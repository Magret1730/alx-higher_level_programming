#!/usr/bin/python3
"""Test cases for class Square"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class Test_Square(unittest.TestCase):
    """class Square test cases"""

    def test_constructor_with_size(self):
        square = Square(5)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)
        self.assertEqual(square.id, 86)

    def test_constructor_with_optional_arguments(self):
        square = Square(7, 2, 3, 10)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 10)

    def test_size_setter(self):
        square = Square(5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_update_method(self):
        square = Square(5)
        square.update(10)
        self.assertEqual(square.id, 10)

    def test_str_method(self):
        square = Square(4, 1, 2, 15)
        self.assertEqual(str(square), "[Square] (15) 1/2 - 4")

    def test_str_method_no_id(self):
        square = Square(3, 0, 0)
        self.assertEqual(str(square), "[Square] (91) 0/0 - 3")

    def test_to_dictionary_method(self):
        square = Square(5, 2, 3, 10)
        expected_dict = {'id': 10, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_is_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(1, 20, 13, 14).__size)

    def test_str_size(self):
        with self.assertRaises(TypeError):
            Square("invalid")

    def test_str_size_None(self):
        with self.assertRaises(TypeError):
            Square(None)

    def test_x_getter(self):
        self.assertEqual(0, Square(10).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(10).y)

    def test_dict_size(self):
        with self.assertRaises(TypeError):
            Square({"a": 19, "b": 25}, 6)

    def test_str_size_str(self):
        with self.assertRaises(TypeError):
            Square("N")

    def test_str_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-6)

    def test_str_size_negative(self):
        with self.assertRaises(TypeError):
            Square(6.7)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)

    def test_None_y(self):
        with self.assertRaises(TypeError):
            Square(1, 3, None)

    def test_str_y(self):
        with self.assertRaises(TypeError):
            Square(1, 1, "invalid")

    def test_area(self):
        s = Square(2, 0, 0, 1)
        s.size = 8
        self.assertEqual(64, s.area())


if __name__ == '__main__':
    unittest.main()
