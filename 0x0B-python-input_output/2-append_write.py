#!/usr/bin/python3
"""A module"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8)

    Args:
        filename: name of file
        text: text to be written in the file

    Returns:
        the number of characters added
    """

    with open(filename, mode="a", encoding="UTF8") as f:
        num_chars = f.write(text)
    return num_chars
