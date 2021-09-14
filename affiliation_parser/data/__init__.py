import json
import os

_root = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(_root, 'university_abbr.json')) as f:
    UNIVERSITY_ABBR = json.load(f)

with open(os.path.join(_root, 'institution.json')) as f:
    INSTITUTE = json.load(f)

with open(os.path.join(_root, 'remove_institution.json')) as f:
    REMOVE_INSTITUE = json.load(f)

with open(os.path.join(_root, 'department.json')) as f:
    DEPARMENT = json.load(f)

with open(os.path.join(_root, 'country.json')) as f:
    COUNTRY = json.load(f)

with open(os.path.join(_root, 'university_multiple_campus.json')) as f:
    UNIVERSITY_MULTIPLE_CAMPUS = json.load(f)

with open(os.path.join(_root, 'states.json')) as f:
    STATES = json.load(f)