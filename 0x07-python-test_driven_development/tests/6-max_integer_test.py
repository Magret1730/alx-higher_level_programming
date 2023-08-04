#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    def test_normal(self):
        """Unittest for max_integer([..])"""
        result = max_integer([4, 9, 3, 5, 6, 1, 0, -6, -4, 10])
        self.assertEqual(result, 10)

    def test_negative_values(self):
        """Unittest for max_integer([..])"""
        result = max_integer([-4, -9, -3, -5, -6, -1, 0, -6, -4, -10])
        self.assertEqual(result, 0)

    def test_empty_list(self):
        """Unittest for max_integer([..])"""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_string(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(['good', 'c', 8, 6])

    def test_set(self):
        """Unittest for max_integer([..])"""
        result = max_integer((4, 6, -9))
        self.assertEqual(result, 6)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer({5, 7, 2, 0})

    def test_zero(self):
        """Unittest for max_integer([..])"""
        result = max_integer([0])
        self.assertEqual(result, 0)

    def test_one_digit(self):
        """Unittest for max_integer([..])"""
        result = max_integer([54])
        self.assertEqual(result, 54)

    def test_one_string(self):
        """Unittest for max_integer([..])"""
        result = max_integer(['d'])
        self.assertEqual(result, 'd')

    def test_multiple_strings(self):
        """Unittest for max_integer([..])"""
        result = max_integer(['girl', 'good', 'lazy'])
        self.assertEqual(result, 'lazy')

    def test_int_string(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(NameError):
            max_integer([d, gh, 67])

    def test_large_numbers(self):
        """Unittest for max_integer([..])"""
        num1 = 4352678987654421343534647585940039898736723645
        num2 = 9876543234567890987654387654321234567890987654342123456
        result = max_integer([num1, num2])
        expected_result = num2
        self.assertEqual(result, expected_result)

    def test_exponentials(self):
        """Unittest for max_integer([..])"""
        result = max_integer([1e5674, 6e3345, 8, 987])
        self.assertEqual(result, float('inf'))

    def test_no_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(56, 87, 97, 34)

    def test_inf(self):
        """Unittest for max_integer([..])"""
        result = max_integer([float('inf')])
        self.assertEqual(result, float('inf'))

    def test_float_int(self):
        """Unittest for max_integer([..])"""
        result = max_integer([56, 87, 97, float('inf')])
        self.assertEqual(result, float('inf'))

    def test_int(self):
        """Unittest for max_integer([..])"""
        result = max_integer([56, 87, 97, int(67)])
        self.assertEqual(result, 97)

    def test_None(self):
        """Unittest for max_integer([..])"""
        result = max_integer([None])
        self.assertEqual(result, None)

    def test_NaN(self):
        """Unittest for max_integer([..])"""
        result = max_integer([float('nan')])
        self.assertTrue(result != result)

    def test_NaN_inf(self):
        """Unittest for max_integer([..])"""
        result = max_integer([1, 2, float('nan'), 4, 5, float('inf')])
        self.assertEqual(result, float('inf'))

    def test_float_nan(self):
        """Unittest for max_integer([..])"""
        result = max_integer([1, 2, float('nan'), 4, 5])
        self.assertEqual(result, 5)

    def test_spaces_comma(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([None, 4, 8, 4, 2])

    def test_None_inbetween(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([None, 4, 8, None, 4, 2])

    def test_space(self):
        """Unittest for max_integer([..])"""
        result = max_integer([4, 8, 4])
        self.assertEqual(result, 8)

    def test_spaces_only(self):
        """Unittest for max_integer([..])"""
        result = max_integer([4, 8, 4, 2])
        self.assertEqual(result, 8)

    def test_list_of_lists(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([8, 6, 3], [1, 2, 5])

    def test_multiple_lists(self):
        """Unittest for max_integer([..])"""
        result = max_integer([[1, 6, 3], [5, 8, 3], [2, 98767, 0]])
        self.assertEqual(result, [5, 8, 3])

    def test_operators(self):
        """Unittest for max_integer([..])"""
        result = max_integer([4+5, 6+7, 1+3])
        self.assertEqual(result, 13)

    def test_operator_mix(self):
        """Unittest for max_integer([..])"""
        result = max_integer([4+5, 6+7, 1+3, 6, 98, 1000+456])
        self.assertEqual(result, 1456)

    def test_float(self):
        """Unittest for max_integer([..])"""
        result = max_integer([9.4555555555, 6.987654, 78, 98, 100000.01])
        self.assertEqual(result, 100000.01)


if __name__ == '__main__':
    unittest.main()
