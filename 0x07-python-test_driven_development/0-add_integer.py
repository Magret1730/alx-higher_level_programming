#!/usr/bin/python3
"""
function that adds 2 integers

and returns the summation of the two integers
"""


def add_integer(a, b=98):
    """function that adds 2 integers.
        the integer of the summation of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
