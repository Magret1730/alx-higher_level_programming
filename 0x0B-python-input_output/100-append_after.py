#!/usr/bin/python3
"""A function"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each
    line containing a specific string
    """
    modified_lines = []
    with open(filename, mode="r", encoding="UTF8") as f:
        for line in f:
            modified_lines.append(line)

            if search_string in line:
                modified_lines.append(new_string)

    with open(filename, mode='w', encoding="UTF8") as f:
        f.writelines(modified_lines)
