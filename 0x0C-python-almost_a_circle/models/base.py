#!/usr/bin/python3
"""A module"""
import json
import turtle


class Base:
    """ A base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor.

        Args:
            id: id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list of instances who inherits of Base - example:
            list of Rectangle or list of Square instances
        """
        filename = cls.__name__ + '.json'
        with open(filename, mode="w", encoding="UTF8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_str = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
                f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
            json_string: string representing a list of dictionaries
        """
        if json_string is None or not json_string:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set

        Args:
            dictionary: can be thought of as a double pointer to a dictionary
            must be used as **kwargs of the method update
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        cls.update(dummy_instance, **dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + '.json'
        instances_list = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                string_from_json = file.read()
                dictionaries_list = cls.from_json_string(string_from_json)
                for dictionary in dictionaries_list:
                    instance = cls.create(**dictionary)
                    instances_list.append(instance)
        except FileNotFoundError:
            pass
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + '.csv'
        with open(filename, mode="w", encoding="UTF8") as f:
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        fields = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        fields = [obj.id, obj.size, obj.x, obj.y]
                    csv_line = ','.join(map(str, fields))
                    f.write(csv_line + '\n')

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + '.csv'
        instances_list = []
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    fields = line.strip().split(',')
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(id=int(fields[0]),
                                              width=int(fields[1]),
                                              height=int(fields[2]),
                                              x=int(fields[3]),
                                              y=int(fields[4]))
                    elif cls.__name__ == "Square":
                        instance = cls.create(id=int(fields[0]),
                                              size=int(fields[1]),
                                              x=int(fields[2]),
                                              y=int(fields[3]))
                    instances_list.append(instance)
        except FileNotFoundError:
            pass
        return instances_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        opens a window and draws all the Rectangles and Squares

        Args:
            list_rectangles: List of Rectangle instances
            list_squares: List of Square instances
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")

        t = turtle.Turtle()
        t.speed(1)  # You can adjust the drawing speed

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for _ in range(2):
                t.forward(rect.width)
                t.right(90)
                t.forward(rect.height)
                t.right(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            for _ in range(4):
                t.forward(square.size)
                t.right(90)

        screen.mainloop()
