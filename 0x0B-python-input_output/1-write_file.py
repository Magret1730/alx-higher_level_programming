#!/usr/bin/python3
"""A module"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)

    Returns:
        the number of characters written
    """

    with open(filename, mode="w", encoding="UTF8") as f:
        num_char = f.write(text)
    return num_char
