#!/usr/bin/python3
"""A class"""


class BaseGeometry:
    """A class with two public instance methods"""

    def area(self):
        """raises Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value, name is always a string"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
