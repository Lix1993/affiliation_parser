from ..data import SUB_REGION


def check_country(affil_text: str):
    """
    Check if any states string from USA or UK
    """
    for region in SUB_REGION:
        for sub_region in SUB_REGION[region]:
            if sub_region in affil_text.lower():
                return region

    return ""
