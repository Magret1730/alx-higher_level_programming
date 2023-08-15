#!/usr/bin/python3
"""A function"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    import json
    json_str = json.dumps(my_obj)
    return json_str
