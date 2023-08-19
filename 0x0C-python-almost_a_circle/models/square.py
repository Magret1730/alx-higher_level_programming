#!/usr/bin/python3
"""
A module that inherits from module Rectangle

A grandchild of class Base and child to class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A module Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor to class Square"""
        super().__init__(size, size, x, y, id)
        # self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """setter for size"""
        self.width = size
        self.height = size

    def __str__(self):
        """
        returns [Square] (<id>) <x>/<y> - <size> - in our case, width or height
        """
        return "[Square] ({}) {}/{} - {}" \
               .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        public method

        Args:
            args: list of arguments
            kwargs: key/value (keyworded arguments)
         """
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
