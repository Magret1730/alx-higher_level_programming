#!/usr/python3
"""Test cases for class Rectangle"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys


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
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, -2, -7, -6, -5)

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
        with self.assertRaises(TypeError):
            r1 = Rectangle("Cohort14", "good", "@", "ing", "rest")

    def test_default_values(self):
        """Test for default values of x and y and id"""
        r1 = Rectangle(34, 56)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

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

    def test_none_all(self):
        """Test None for all"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None, None, None)

    # Area test cases
    def test_area(self):
        """Test for Area()"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_area1(self):
        """Test for Area1()"""
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_area_string(self):
        """Test for width strings"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("G", 8)
            r1.area()

    def test_area_string1(self):
        """Test for height strings"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(8, "G")
            r1.area()

    def test_area_string2(self):
        """Test for invalid width strings"""
        with self.assertRaises(NameError):
            r1 = Rectangle(G, 8)
            r1.area()

    def test_area_string3(self):
        """Test for invalid height strings"""
        with self.assertRaises(NameError):
            r1 = Rectangle(8, G)
            r1.area()

    def test_area_large_values(self):
        """Test for large values"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1e676, 15e65)
            r1.area()

    def test_area_none(self):
        """Test for None"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None)
            r1.area()

    def test_area_none_width(self):
        """Test for None on width"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 5)
            r1.area()

    def test_area_none_height(self):
        """Test for None on height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, None)
            r1.area()

    def test_area_negative_values_area(self):
        """Negative values test"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, -2)
            r1.area()

    def test_area_negative_width(self):
        """Negative values test on width"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)
            r1.area()

    def test_area_negative_height(self):
        """Negative values test on height"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2)
            r1.area()

    def test_area_zero(self):
        """Test for area zero"""
        r1 = Rectangle(0, 0)
        self.assertEqual(r1.area(), 0)

    def test_area_width_zero(self):
        """Test for area zero width"""
        r1 = Rectangle(0, 4)
        self.assertEqual(r1.area(), 0)

    def test_area_height_zero(self):
        """Test for area zero height"""
        r1 = Rectangle(5, 0)
        self.assertEqual(r1.area(), 0)

    def test_area_large_numbers(self):
        """Test for large area value"""
        r1 = Rectangle(1000, 10000)
        self.assertEqual(r1.area(), 1000 * 10000)

    def test_extra_large_numbers_area(self):
        """Test for very large area value"""
        r1 = Rectangle((10**6), (10**7))
        self.assertEqual(r1.area(), (10**6) * (10**7))

    # display
    # large numbers is missing
    def test_display_normal(self):
        """Test for normal values"""
        captured_output = StringIO()
        sys.stdout = captured_output
        expected_output = "####\n" * 6 + "\n"
        r1 = Rectangle(4, 6)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(),
                         expected_output.strip())

    def test_display_zero_width(self):
        """Test display with width of 0"""
        r = Rectangle(0, 5)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = ""
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_display_zero_height(self):
        """Test display with height of 0"""
        r = Rectangle(5, 0)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = ""
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_display_zero_dimensions(self):
        """Test display with both dimensions as 0"""
        r = Rectangle(0, 0)
        captured_output = StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        expected_output = ""
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_display_negative_width(self):
        """Test display with negative width"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 4)
            r.display()

    def test_display_negative_height(self):
        """Test display with negative height"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, -4)
            r.display()

    def test_display_negative_dimensions(self):
        """Test display with negative dimensions"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, -4)
            r.display()

    def test_display_string_width(self):
        """Test display with width as a string"""
        with self.assertRaises(TypeError):
            r = Rectangle("5", 4)
            r.display()

    def test_display_string_height(self):
        """Test display with height as a string"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, "4")
            r.display()

    def test_display_string_dimensions(self):
        """Test display with both width and height as strings"""
        with self.assertRaises(TypeError):
            r = Rectangle("5", "4")
            r.display()

    def test_display_string(self):
        """Test for width strings"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("G", 8)
            r1.display()

    def test_display_string1(self):
        """Test for height strings"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(8, "G")
            r1.display()

    def test_display_string2(self):
        """Test for invalid width strings"""
        with self.assertRaises(NameError):
            r1 = Rectangle(G, 8)
            r1.display()

    def test_display_string3(self):
        """Test for invalid height strings"""
        with self.assertRaises(NameError):
            r1 = Rectangle(8, G)
            r1.display()

    def test_display_large_values(self):
        """Test for large values"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1e676, 15e65)
            r1.display()

    def test_display_none(self):
        """Test for None"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None)
            r1.display()

    def test_display_none_width(self):
        """Test for None on width"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 5)
            r1.display()

    def test_display_none_height(self):
        """Test for None on height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(5, None)
            r1.display()


if __name__ == "__main__":
    unittest.main()
