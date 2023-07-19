#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return None
    new_set = []
    for values in set_1:
        for elements in set_2:
            if values == elements:
                new_set.append(values)
    return new_set
