#!/usr/bin/python3
"""A function"""


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string
    """

    import json
    txt_from_json = json.loads(my_str)
    return txt_from_json
