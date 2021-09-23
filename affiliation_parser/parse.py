import re

import numpy as np
from unidecode import unidecode

from .data import INSTITUTE
from .parser import (append_institution_city, check_country, clean_text,
                     replace_institution_abbr, parse_email, parse_location,
                     parse_zipcode)


def parse_affil(affil_text):
    """
    Parse affiliation string to institution and department
    """
    dict_out = {
        "full_text": '',
        "divide": '',
        "sub_divides": [],
        "institution": '',
        "email": '',
        "zipcode": '',
        "country": ''
    }

    affil_text = unidecode(affil_text)
    affil_text = clean_text(affil_text)

    affil_text = replace_institution_abbr(affil_text)
    email = parse_email(affil_text)
    dict_out["email"] = email
    affil_text = re.sub(re.escape(email), "", affil_text)

    zip_code = parse_zipcode(affil_text)
    dict_out["zipcode"] = zip_code
    affil_text = re.sub(zip_code, "", affil_text)

    affil_list = affil_text.split(", ")

    institution_list = list()
    location_list = list()

    for i, a in enumerate(affil_list):
        for ins in INSTITUTE:
            if ins in a.lower():
                institution_list.append((a, INSTITUTE[ins]))
                location_list = affil_list[i + 1::]
                break

    for i in range(1, len(institution_list)):
        if institution_list[i][1] > institution_list[i - 1][1]:
            return dict_out
    if [i[1] for i in institution_list].count(1) > 1:
        return dict_out

    institution_list = [i[0] for i in institution_list]
    for i, affi in enumerate(institution_list):
        for term in ["hospital"]:
            if term in affi[0].lower():
                hospital = ', '.join(institution_list[i:])
                institution_list = institution_list[:i] + [hospital]

    # # remove unwanted from affliation list and location list
    # pop_index = list()
    # for i, a in enumerate(institution_list):
    #     for rm in REMOVE_INSTITUE:
    #         if rm in a.lower() and (not "university" in a.lower()):
    #             pop_index.append(i)
    # institution_list = np.delete(institution_list,
    #                              list(set(pop_index))).tolist()

    # department_list = list()
    # for i, a in enumerate(affil_list):
    #     for dep in DEPARMENT:
    #         if dep in a.lower() and (not a in department_list):
    #             department_list.append(affil_list[i])
    # department = ", ".join(department_list)

    pop_index = list()
    for i, l in enumerate(location_list):
        for rm in INSTITUTE:
            if rm in l.lower():
                pop_index.append(i)
    location_list = np.delete(location_list, list(set(pop_index))).tolist()

    location = ", ".join(location_list)
    if location == "":
        location = affil_list[-1]
    location = re.sub(r"\([^)]*\)", "", location).strip()

    dict_location = parse_location(location)

    institution = ''
    divide = ''
    sub_devides = []
    if len(institution_list) > 0:
        institution = institution_list[-1]
        if len(institution_list) > 1:
            divide = institution_list[-2]
            if len(institution_list) > 2:
                sub_devides = institution_list[:-2]

    institution = append_institution_city(institution,
                                          dict_location["location"])

    dict_out["full_text"] = affil_text.strip().strip('.')
    dict_out["institution"] = institution.strip().strip()
    dict_out["divide"] = divide.strip().strip('.')
    dict_out["sub_devides"] = [i.strip().strip('.') for i in sub_devides]

    dict_out.update(dict_location)

    if dict_out["country"] == "":
        dict_out["country"] = check_country(affil_text)  # check country

    return dict_out
