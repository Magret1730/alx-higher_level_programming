#!/usr/bin/python3
"""A function"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    import json
    with open(filename, mode="w", encoding="UTF8") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
