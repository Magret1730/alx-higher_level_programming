#!/usr/bin/python3
def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    max_number = 0
    if len(list_of_integers) == 0:
        return None
    for i in list_of_integers:
        if i > max_number:
            max_number = i
    return max_number
