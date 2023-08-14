#!/usr/bin/python3
"""A module"""


def add_attribute(obj, attribute, value):
    """
    adds a new attribute to an object if it’s possible

    Args:
        obj: The object to which the attribute is to be added.
        attribute: The name of the attribute to be added.
        value: The value of the attribute to be added.

    Raises:
        TypeError: If the object can't have new attributes.
    """

    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
