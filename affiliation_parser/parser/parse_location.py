import re

from ..data import REGION_ALIAS


def get_joined_elements(words, number):
    result = []

    for i in range(len(words) - number + 1):
        result.append(' '.join(words[i:i + number]))

    return result


def find_country(location: str):
    """
    Find country from string list
    """
    location_lower = location.lower().strip(' .')
    splits = re.split(r'\.\s|,|;|\(|\)', location_lower)
    splits = [i.strip().lower() for i in splits if i]

    # single word match country name or alias
    for country in REGION_ALIAS:
        if set(REGION_ALIAS[country]).intersection(set(splits)):
            return country

    # two words or more to match
    double_elems = get_joined_elements(splits[-4:], 2)
    triple_elems = get_joined_elements(splits[-4:], 3)
    quadruple_elems = get_joined_elements(splits[-4:], 4)
    word_tuple = double_elems + triple_elems + quadruple_elems
    for country in REGION_ALIAS:
        if set(REGION_ALIAS[country]).intersection(set(word_tuple)):
            return country

    return ""


def parse_location(location):
    """
    Parse location and country from affiliation string
    """

    country = find_country(location)
    dict_location = {"location": location.strip(), "country": country.strip()}
    return dict_location
