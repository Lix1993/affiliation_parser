import re

from ..data import REGION_ALIAS


def find_country(location: str):
    """
    Find country from string
    """
    location_lower = location.lower()
    for alias in REGION_ALIAS:
        if alias in location_lower:
            return REGION_ALIAS[alias]
    return ""


def parse_location(location):
    """
    Parse location and country from affiliation string
    """
    location = re.sub(r"\.", "", location).strip()
    country = find_country(location)
    dict_location = {"location": location.strip(), "country": country.strip()}
    return dict_location
