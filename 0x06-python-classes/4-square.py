#!/usr/bin/python3
"""A Square class"""


class Square:
    """a class Square that defines a square"""

    def __init__(self, size=0):
        """a module with private instance attribute size

        using getters and setters.

        Args:
        size: size of a square

        Raises:
        ValueError: if size is less than zero
        TypeError: if size is not int
        """

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns current square area"""

        return self.__size**2
