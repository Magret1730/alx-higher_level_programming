#!/usr/bin/python3
"""A module inheriting from class Base"""
from .base import Base


class Rectangle(Base):
    """A class inheriting from super class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor.

        Args:
            width: width
            height: height
            x: 0
            y: 0
            id: id
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for private instance attribute x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for private instance attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter for private instance attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        rect = ""
        for i in range(self.__y):
            rect += '\n'
        for j in range(self.__height):
            rect += ' ' * self.__x + '#' * self.__width + '\n'
        # rect += "#"
        # if i != (self.__height - 1):
        # rect = rect + '\n'
        print(rect, end="")

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
