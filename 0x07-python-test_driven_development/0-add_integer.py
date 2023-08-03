#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """function that adds 2 integers.

    Args:
    a: first integer
    b: second integer with a constant value 98

    return: the integer of the summation of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
