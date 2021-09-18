import json
import os

_root = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(_root, 'institution_abbr.json')) as f:
    UNIVERSITY_ABBR = json.load(f)

with open(os.path.join(_root, 'institution_educational.json')) as f:
    INSTITUTE_EDUCATIONAL = json.load(f)

with open(os.path.join(_root, 'institution_commercial.json')) as f:
    INSTITUTE_COMMERCIAL = json.load(f)

with open(os.path.join(_root, 'multiple_campus.json')) as f:
    MULTIPLE_CAMPUS = json.load(f)

with open(os.path.join(_root, 'region_alias.json')) as f:
    REGION_ALIAS = json.load(f)

with open(os.path.join(_root, 'sub_region.json')) as f:
    SUB_REGION = json.load(f)

# with open(os.path.join(_root, 'remove_institution.json')) as f:
#     REMOVE_INSTITUE = json.load(f)

# with open(os.path.join(_root, 'department.json')) as f:
#     DEPARMENT = json.load(f)
