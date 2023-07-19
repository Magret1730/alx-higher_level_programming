#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for values in b_dictionary:
        b_dictionary[values] *= 2
    return b_dictionary
