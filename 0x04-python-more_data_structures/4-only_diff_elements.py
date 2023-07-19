#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None
    new_set = set_1 ^ set_2
    return new_set
