from ..data import MULTIPLE_CAMPUS


def append_institution_city(affil: str, location: str):
    """
    Append city to university that has multiple campuses if exist
    """
    for university in MULTIPLE_CAMPUS:
        if university in affil.lower():
            for city in MULTIPLE_CAMPUS[university]:
                if city in location.lower() and not city in affil.lower():
                    affil = affil + ", " + city
                    return affil
    return affil
