 
# JSON to python

import json
json_str = ' {"name": "Draupdi", "isTeacher": true}'
py_obj = json.loads(json_str)
print(type(py_obj), py_obj)

# OUTPUT -    <class 'dict'> {'name': 'Draupdi', 'isTeacher': True}

#_______________________________________________________________________________________________________

# Python to JSON

import json

py_lines = {
    "name": "Arjun",
    "isAlive": False,
    "Medals_won": None
}

json_lines = json.dumps(py_lines)
print(type(json_lines), json_lines)


# OUTPUT -    <class 'str'> {"name": "Arjun", "isAlive": false, "Medals_won": null}