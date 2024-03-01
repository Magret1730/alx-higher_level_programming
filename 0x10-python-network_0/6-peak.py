#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers
    max_number = 0
    if len(list_of_integers) == 0:
        return None
    for i in list_of_integers:
        if i > max_number:
            max_number = i
    return max_number"""

    left = 0
    right = len(list_of_integers) - 1

    if len(list_of_integers) == 0:
        return None
    while left < right:  # Adjust the loop condition
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return list_of_integers[left]
