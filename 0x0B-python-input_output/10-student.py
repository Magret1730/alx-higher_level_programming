#!/usr/bin/python3
"""A module"""


class Student:
    """A class student"""

    def __init__(self, first_name, last_name, age):
        """
        Constructor with public instance attributes

        Args:
            first_name
            last_name
            age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        # If attrs is a list of strings, only attribute names contained
        # in this list must be retrieved.
        # Otherwise, all attributes must be retrieved
        new_dict = self.__dict__
        if attrs is None:
            return new_dict
        else:
            for attr in attrs:
                if attr in new_dict:
                    return {attr: new_dict[attr]}
