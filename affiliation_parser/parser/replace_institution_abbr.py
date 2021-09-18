import re

from ..data import UNIVERSITY_ABBR


def replace_institution_abbr(affil_text: str):
    """
    Replace abbreviation with full institution string
    """
    for university in UNIVERSITY_ABBR:
        for abbr in UNIVERSITY_ABBR[university]:
            if abbr in affil_text:
                affil_text = re.sub(abbr, university, affil_text)
                return affil_text
    return affil_text
