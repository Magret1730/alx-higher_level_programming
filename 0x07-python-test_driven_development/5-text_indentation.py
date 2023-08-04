#!/usr/bin/python3
"""
function that prints

a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints

    a text with 2 new lines after each of these characters: ., ? and :
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_text = ""
    for char in text:
        new_text += char
        if char in ".?:":
            new_text += "\n\n"

    lines = new_text.splitlines()
    cleaned_lines = [line.strip() for line in lines]
    result = "\n".join(cleaned_lines)
    if result.endswith("\n"):
        result = result[:-1]
    print("{}".format(result), end="")
