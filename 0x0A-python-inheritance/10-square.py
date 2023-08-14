#!/usr/bin/python3
"""A module for class Rectangle"""


class BaseGeometry:
    """A class with two public instance methods"""

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
        self._width = width
        self._height = height

    def area(self):
        """calculates area of rectangle"""

        return self._width * self._height

    def __str__(self):
        """returns [Rectangle] <width>/<height>"""

        return "[Rectangle] {}/{}".format(self._width, self._height)


class Square(Rectangle):
    """a subclass of superclass Rectangle"""

    def __init__(self, size):
        """Constructor with validation"""

        self.integer_validator("size", size)
        self._size = size

    def area(self):
        """calculates the area of square"""

        return self._size ** 2

    def __str__(self):
        """returns a printed format"""

        return "[Rectangle] {}/{}".format(self._size, self._size)
