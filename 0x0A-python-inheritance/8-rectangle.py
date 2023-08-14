#!/usr/bin/python3
"""A module for class Rectangle"""


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


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from class BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
