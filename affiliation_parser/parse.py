import re

import numpy as np
from unidecode import unidecode

from .data import DEPARMENT, INSTITUTE, REMOVE_INSTITUE
from .parser import (append_institution_city, check_country, clean_text,
                     parse_email, parse_location, parse_zipcode)


def parse_affil(affil_text):
    """
    Parse affiliation string to institution and department
    """
    affil_text = unidecode(affil_text)
    affil_text = clean_text(affil_text)

    # affil_text = replace_institution_abbr(affil_text)
    email = parse_email(affil_text)
    affil_text = re.sub(email, "", affil_text)

    zip_code = parse_zipcode(affil_text)
    affil_text = re.sub(zip_code, "", affil_text)

    affil_list = affil_text.split(", ")

    institution_list = list()
    location_list = list()

    for i, a in enumerate(affil_list):
        for ins in INSTITUTE:
            if ins in a.lower() and (not a in institution_list):
                institution_list.append(a)
                location_list = affil_list[i + 1::]

    # remove unwanted from affliation list and location list
    pop_index = list()
    for i, a in enumerate(institution_list):
        for rm in REMOVE_INSTITUE:
            if rm in a.lower() and (not "university" in a.lower()):
                pop_index.append(i)
    institution_list = np.delete(institution_list,
                                 list(set(pop_index))).tolist()

    pop_index = list()
    for i, l in enumerate(location_list):
        for rm in DEPARMENT:
            if rm in l.lower():
                pop_index.append(i)
    location_list = np.delete(location_list, list(set(pop_index))).tolist()

    institution = ", ".join(institution_list)
    location = ", ".join(location_list)
    if location == "":
        location = affil_list[-1]
    location = re.sub(r"\([^)]*\)", "", location).strip()

    department_list = list()
    for i, a in enumerate(affil_list):
        for dep in DEPARMENT:
            if dep in a.lower() and (not a in department_list):
                department_list.append(affil_list[i])
    department = ", ".join(department_list)

    dict_location = parse_location(location)

    institution = append_institution_city(institution,
                                          dict_location["location"])

    dict_out = {
        "full_text": affil_text.strip(),
        "department": department.strip(),
        "institution": institution.strip(),
        "email": email,
        "zipcode": zip_code,
    }
    dict_out.update(dict_location)
    if dict_out["country"] == "":
        dict_out["country"] = check_country(affil_text)  # check country
    return dict_out
