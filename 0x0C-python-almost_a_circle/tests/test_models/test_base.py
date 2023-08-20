#!/usr/bin/python3
"""Test cases for Python: Almost a circle project"""


import turtle
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Base(unittest.TestCase):
    """Test cases"""

    def test_id_provided(self):
        """Test for if id is provided"""
        b1 = Base(id=5)
        self.assertEqual(b1.id, 5)

    def test_no_id_provided(self):
        """Test without id"""
        case1 = Base()
        case2 = Base()
        self.assertEqual(case1.id, 25)
        self.assertEqual(case2.id, 26)

    def test_multiple_instances(self):
        """Testing for multiple instances of Base"""
        cases = [Base() for _ in range(7)]
        self.assertEqual([case.id for case in cases],
                         [18, 19, 20, 21, 22, 23, 24])

    def test_private_attribute(self):
        """Test for directly accessing the class private instance"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_different_ids(self):
        """Test for different ids"""
        b1 = Base(12)
        b2 = Base()
        b3 = Base(50)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 7)
        self.assertEqual(b3.id, 50)

    def test_negative_ids(self):
        """Test for negative ids"""
        b1 = Base(-4)
        self.assertEqual(b1.id, -4)

    def test_id_zero(self):
        """Test for id is zero"""
        b1 = Base(0)
        self.assertEqual(b1.id, 0)

    # to_json_string
    def test_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_none_list(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_single_item_list(self):
        data = [{"id": 1, "x": 0, "y": 0}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "x": 0, "y": 0}]')

    def test_multiple_items_list(self):
        data = [{"id": 1, "x": 0, "y": 0}, {"id": 2, "x": 10, "y": 20}]
        result = Base.to_json_string(data)
        expected_result = ('[{"id": 1, "x": 0, "y": 0}, '
                           '{"id": 2, "x": 10, "y": 20}]')
        self.assertEqual(result, expected_result)

    def test_nested_dicts(self):
        data = [{"id": 1, "coordinates": {"x": 0, "y": 0}},
                {"id": 2, "coordinates":
                {"x": 10, "y": 20}}]
        result = Base.to_json_string(data)
        expected_result = json.dumps(data)
        self.assertEqual(result, expected_result)

    def test_special_characters(self):
        data = [{"id": 1, "name": "John Doe", "city": "New York"}]
        result = Base.to_json_string(data)
        expected_result = '[{"id": 1, "name": "John Doe", "city": "New York"}]'
        self.assertEqual(result, expected_result)

    def test_large_list(self):
        data = [{"id": i, "value": i * 10} for i in range(1000)]
        result = Base.to_json_string(data)
        expected_result = json.dumps(data)
        self.assertEqual(result, expected_result)

    def test_empty_dict_in_list(self):
        data = [{}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{}]')

    def test_nested_empty_dict_in_list(self):
        data = [{"id": 1, "info": {}}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "info": {}}]')

    def test_nested_empty_list_in_dict(self):
        data = [{"id": 1, "values": []}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "values": []}]')

    def test_unicode_characters(self):
        data = [{"id": 1, "message": "Hello, \u03A9"}]
        result = Base.to_json_string(data)
        expected_result = '[{"id": 1, "message": "Hello, \\u03a9"}]'
        self.assertEqual(result, expected_result)

    def test_special_values(self):
        data = [{"id": 1, "value": None}, {"id": 2, "value": True},
                {"id": 3, "value": False}]
        result = Base.to_json_string(data)
        expected_result = ('[{"id": 1, "value": null}, '
                           '{"id": 2, "value": true}, '
                           '{"id": 3, "value": false}]')
        self.assertEqual(result, expected_result)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 4)

    # json to string
    def test_save_none_list(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    def test_save_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    """
    def test_save_squares(self):
        s1 = Square(6)
        s2 = Square(3)
        Base.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            content = file.read()
            expected_content = '[{"id": 12, "x": 0, "size": 5, "y": 0},
                                 {"id": 13, "x": 9, "size": 7, "y": 1}]'
            self.assertEqual(content, expected_content)
    """

    def test_save_nested_dicts(self):
        r1 = Rectangle(10, 5)
        data = [{"id": 1, "info": {"width": 5, "height": 2}}]
        Base.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected_content = ('[{"x": 2, "y": 8, "id": 8, "height": 7, '
                                '"width": 10}, {"x": 0, "y": 0, "id": 9, '
                                '"height": 4, "width": 2}]')
            self.assertEqual(content, expected_content)

    """
    def test_save_special_characters(self):
        s1 = Square(5, 0, 0, "Hello, \u03A9")
        Base.save_to_file([s1])
        with open("Square.json", "r") as file:
            content = file.read()
            expected_content = '[{"id": 12, "x": 0, "size": 5, "y": 0},
                                 {"id": 13, "x": 9, "size": 7, "y": 1}]'
            self.assertEqual(content, expected_content)
    """

    def test_save_empty_list_of_objects(self):
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, "[]")

    # from_json_string
    def test_from_json_string_empty(self):
        result = Base.from_json_string("")
        self.assertEqual(result, '[]')

    def test_from_json_string_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, '[]')

    def test_from_json_string_single_item(self):
        json_string = '[{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}]'
        expected_result = [{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_from_json_string_multiple_items(self):
        json_string = '[{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0}, \
                        {"id": 2, "size": 3, "x": 0, "y": 0}]'
        expect_result = [{"id": 1, "width": 10, "height": 5, "x": 0, "y": 0},
                         {"id": 2, "size": 3, "x": 0, "y": 0}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expect_result)

    def test_from_json_string_invalid_json(self):
        invalid_json = '{"id": 1, "width": 10, "height": 5'
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string(invalid_json)

    def test_from_json_string_nested_dicts(self):
        json_string = '[{"id": 1, "rect": {"width": 10, "height": 5}}, \
                        {"id": 2, "sq": {"size": 3}}]'
        expected_result = [
            {"id": 1, "rect": {"width": 10, "height": 5}},
            {"id": 2, "sq": {"size": 3}}
        ]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_from_json_string_unicode_characters(self):
        json_string = '[{"id": 1, "text": "Hello, Ω"}]'
        expected_result = [{"id": 1, "text": "Hello, Ω"}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_from_json_string_invalid_nested_dicts(self):
        json_string = '[{"id": 1, "rect": {"width": 10, "height": 5}, \
                        "extra": "data"}, \
                        {"id": 2, "sq": {"size": 3}}]'
        expected_result = [{"id": 1, "rect": {"width": 10, "height": 5},
                           "extra": "data"},
                           {"id": 2, "sq": {"size": 3}}]
        result = Base.from_json_string(json_string)
        self.assertEqual(result, expected_result)

    def test_from_json_string_malformed_json(self):
        malformed_json = '[{"id": 1, "width": 10, "height": 5], \
                           {"id": 2, "size": 3}]'  # Missing opening brace
        with self.assertRaises(json.JSONDecodeError):
            Base.from_json_string(malformed_json)

    # create
    def test_create_rectangle(self):
        dummy_instance = Rectangle(1, 1)
        dummy_instance_dict = dummy_instance.to_dictionary()
        instance = Rectangle.create(**dummy_instance_dict)
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.width, dummy_instance.width)
        self.assertEqual(instance.height, dummy_instance.height)

    def test_create_square(self):
        dummy_instance = Square(1)
        dummy_instance_dict = dummy_instance.to_dictionary()
        instance = Square.create(**dummy_instance_dict)
        self.assertIsInstance(instance, Square)
        self.assertEqual(instance.size, dummy_instance.size)

    def test_create_with_additional_attributes(self):
        dummy_instance = Rectangle(1, 1)
        dummy_instance_dict = dummy_instance.to_dictionary()
        dummy_instance_dict['extra'] = 42  # Adding an extra attribute
        instance = Rectangle.create(**dummy_instance_dict)
        self.assertIsInstance(instance, Rectangle)
        self.assertEqual(instance.width, dummy_instance.width)
        self.assertEqual(instance.height, dummy_instance.height)
        self.assertFalse(hasattr(instance, 'extra'))

    # load_from_file
    def test_load_from_nonexistent_file(self):
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)

    def test_load_from_file_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 7)
        self.assertEqual(instances[0].x, 2)
        self.assertEqual(instances[0].y, 8)

    def test_load_from_file_square(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Square)
        self.assertEqual(instances[0].size, 5)
        self.assertEqual(instances[0].x, 0)
        self.assertEqual(instances[0].y, 0)

    def test_load_from_empty_file(self):
        with open("Rectangle.json", "w") as file:
            file.write("[]")
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 0)

    """
    def test_load_from_invalid_file_format(self):
        with open("Square.json", "w") as file:
            file.write("Invalid JSON content")
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 0)
    """

    # others
    def test_type_rectangle(self):
        """Test for type rectangle"""
        self.assertIsInstance(Rectangle(12, 45), Base)

    # CSV
    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
            os.remove("Square.csv")
        except OSError:
            pass

    def test_save_and_load_rectangle_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        instances = Rectangle.load_from_file_csv()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Rectangle)
        self.assertEqual(instances[0].width, 10)
        self.assertEqual(instances[0].height, 7)
        self.assertEqual(instances[0].x, 2)
        self.assertEqual(instances[0].y, 8)

    def test_save_and_load_square_csv(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        instances = Square.load_from_file_csv()
        self.assertEqual(len(instances), 2)
        self.assertIsInstance(instances[0], Square)
        self.assertEqual(instances[0].size, 5)
        self.assertEqual(instances[0].x, 0)
        self.assertEqual(instances[0].y, 0)

    def test_save_and_load_empty_csv(self):
        with open("Rectangle.csv", "w") as file:
            file.write("")
        instances = Rectangle.load_from_file_csv()
        self.assertEqual(len(instances), 0)

    def test_save_and_load_mixed_instances_csv(self):
        r1 = Rectangle(10, 7)
        s1 = Square(5)
        Rectangle.save_to_file_csv([r1])
        Square.save_to_file_csv([s1])
        instances = Base.load_from_file_csv()
        self.assertEqual(len(instances), 0)

    """
    # turtle
    def test_draw_rectangles_and_squares(self):
        r1 = Rectangle(100, 50, 50, 50)
        r2 = Rectangle(70, 70, 10, 10)
        s1 = Square(80, 20, 20)
        s2 = Square(40, 80, 80)
        Base.draw([r1, r2], [s1, s2])
        turtle.done()
    """


if __name__ == '__main__':
    unittest.main()
