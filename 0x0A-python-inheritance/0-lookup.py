#!/usr/bin/python3
"""A function"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""

    # atrributes_and_methods = []
    # for attributes in dir(obj):
        # print(attributes)
        # atrributes_and_methods.append(attributes)
    # return atrributes_and_methods

    return dir(obj)
