#!/usr/bin/python3
"""
A module for class Rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializer

        Args:
            width - width
            height - height

        Raises:
            TypeError if attribute is not an integer
            ValueError if attribute is less than 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """
        property of width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """
        property of height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
