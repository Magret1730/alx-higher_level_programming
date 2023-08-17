#!/usr/python3
"""Test cases for class Rectangle"""
import unittest
from models.rectangle import Rectangle


class Test_rectangle(unittest.TestCase):
    """class Rectangle test cases"""

    def test_normal1(self):
        """Normal tests"""
        r1 = Rectangle(10, 2, 7, 6, 5)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 6)

    def test_negative_values(self):
        """Negative values test"""
        r1 = Rectangle(-10, -2, -7, -6, -5)
        self.assertEqual(r1.id, -5)
        self.assertEqual(r1.width, -10)
        self.assertEqual(r1.height, -2)
        self.assertEqual(r1.x, -7)
        self.assertEqual(r1.y, -6)

    def test_large_values(self):
        """Test for large values"""
        r1 = Rectangle(10000, 20000, 70000, 60000, 50000)
        self.assertEqual(r1.id, 50000)
        self.assertEqual(r1.width, 10000)
        self.assertEqual(r1.height, 20000)
        self.assertEqual(r1.x, 70000)
        self.assertEqual(r1.y, 60000)

    # strings for each keywords
    def test_height(self):
        """Test for width and height"""
        r1 = Rectangle(34, 56)
        self.assertEqual(r1.width, 34)
        self.assertEqual(r1.height, 56)

    def test_strings(self):
        """Test for strings in the parameters"""
        r1 = Rectangle("Cohort14", "good", "@", "ing", "rest")
        self.assertEqual(r1.width, "Cohort14")
        self.assertEqual(r1.height, "good")
        self.assertEqual(r1.x, "@")
        self.assertEqual(r1.y, "ing")
        self.assertEqual(r1.id, "rest")

    def test_default_values(self):
        """Test for default values of x and y and id"""
        r1 = Rectangle(34, 56)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_invalid(self):
        """Test for invalid inputs"""
        with self.assertRaises(NameError):
            r1 = Rectangle(Cohort14, good)

    def test_invalid1(self):
        """Test for invalid inputs"""
        with self.assertRaises(NameError):
            r1 = Rectangle(Cohort14, "good", 8, 9, 0)

    def test_id_zero(self):
        """Test for id is zero"""
        r1 = Rectangle(3, 5, id=0)
        self.assertEqual(r1.id, 0)

    def test_x(self):
        """Test for x"""
        r1 = Rectangle(3, 5, x=5)
        self.assertEqual(r1.x, 5)
