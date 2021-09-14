import re

from ..data import COUNTRY


def find_country(location: str):
    """
    Find country from string
    """
    location_lower = location.lower()
    for country in COUNTRY:
        for c in COUNTRY[country]:
            if c in location_lower:
                return country
    return ""


def parse_location(location):
    """
    Parse location and country from affiliation string
    """
    location = re.sub(r"\.", "", location).strip()
    country = find_country(location)
    dict_location = {"location": location.strip(), "country": country.strip()}
    return dict_location
