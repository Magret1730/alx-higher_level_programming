#!/usr/bin/python3
"""
A module for class Rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def area(self):
        """returns the rectangle area"""

        return self.__width * self.__height

    def perimeter(self):
        """ returns the rectangle perimeter"""

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """print the rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect = rect + '#'
            if i != (self.__height - 1):
                rect = rect + '\n'
        return rect

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deletes an instance of Rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
