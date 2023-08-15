#!/usr/bin/python3
"""A function"""


def load_from_json_file(filename):
    """creates an Object from a 'JSON file'"""

    import json
    with open(filename, encoding="UTF8") as f:
        obj_from_json = json.load(f)
    return obj_from_json
