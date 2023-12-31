#!/usr/bin/python3
"""
function that prints

function that prints a square with the character #
"""


def print_square(size):
    """
    function that prints a square with the character #
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for value in range(size):
        for j in range(size):
            print("#", end="")
        print()
