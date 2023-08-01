#!/usr/bin/python3
"""A Square class"""


class Square:
    """a class Square that defines a square"""

    def __init__(self, size=0):
        """a module with private instance attribute size

        Args:
        size: size of a square

        Raises:
        ValueError: if size is less than zero
        TypeError: if size is not int
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
