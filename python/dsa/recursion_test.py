"""
recursion_test.py: Test cases for recursion algorithms.
"""

__author__ = 'nehar'

import unittest
from recursion import factorial
from recursion import Ruler



class TestRecursion(unittest.TestCase):

    def test_factorial(self):
        """

        :return:
        """
        self.assertEquals(1, factorial(0))
        self.assertEquals(1, factorial(1))
        self.assertEquals(2, factorial(2))
        self.assertEquals(6, factorial(3))
        self.assertEquals(3628800, factorial(10))
        self.assertEquals(1307674368000, factorial(15))

        with self.assertRaises(ValueError):
            factorial(3/2)
        with self.assertRaises(ValueError):
            factorial(-4)

    def test_ruler(self):
        """

        :return:
        """
        # TODO: fix - test, instead of printing...
        x = "---- 0\n-\n--\n-\n---\n-\n--\n-\n---- 1\n-\n--\n-\n---\n-\n--\n-\n---- 2\n"
        self.assertEquals(x, Ruler(inches=2, major_length=4).draw())
        print("\n\n"*5)

        x = "----- 0\n-\n--\n-\n---\n-\n--\n-\n----\n-\n--\n-\n---\n-\n--\n-\n----- 1\n"
        self.assertEquals(x, Ruler(inches=1, major_length=5).draw())
        print("\n\n"*5)

        x = """--- 0\n-\n--\n-\n--- 1\n-\n--\n-\n--- 2\n-\n--\n-\n--- 3\n"""
        self.assertEqual(x, Ruler(inches=3, major_length=3).draw())
