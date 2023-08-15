#!/usr/bin/python3
"""A function file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open(filename, mode='r', encoding='UTF8') as f:
        for lines in f:
            print(lines, end="")
