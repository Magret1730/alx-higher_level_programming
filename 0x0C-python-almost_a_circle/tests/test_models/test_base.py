#!/usr/bin/python3
"""Test cases for Python: Almost a circle project"""


import unittest
from models.base import Base


class test_Base(unittest.TestCase):
    """Test cases"""

    def test_id_provided(self):
        """Test for if id is provided"""
        b1 = Base(id=5)
        self.assertEqual(b1.id, 5)

    """def test_no_id_provided(self):
        Test without id
        case1 = Base()
        case2 = Base()
        self.assertEqual(cases.id, 1)
        self.assertEqual(b2.id, 2)"""

    """def test_multiple_instances(self):
        Testing for multiple instances of Base
        cases = [Base() for _ in range(7)]
        self.assertEqual([case.id for case in cases], [1, 2, 3, 4, 5, 6, 7])"""

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
        self.assertEqual(b2.id, 1)
        self.assertEqual(b3.id, 50)

    def test_negative_ids(self):
        """Test for negative ids"""
        b1 = Base(-4)
        self.assertEqual(b1.id, -4)

    """def test_large_no_instances(self):
        Test for large number of instances
        ins = 15000
        cases = [Base() for _ in range(ins)]
        self.assertEqual([case.id for case in cases], list(range(1, ins + 1)))
    """


if __name__ == '__main__':
    unittest.main()
