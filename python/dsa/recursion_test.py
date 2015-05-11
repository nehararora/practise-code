"""
recursion_test.py: Test cases for recursion algorithms.
"""

__author__ = 'nehar'

import unittest
import recursion


class TestRecursion(unittest.TestCase):
    def test_factorial(self):
        """

        :return:
        """
        self.assertEquals(1, recursion.factorial(0))
        self.assertEquals(1, recursion.factorial(1))
        self.assertEquals(2, recursion.factorial(2))
        self.assertEquals(6, recursion.factorial(3))
        self.assertEquals(3628800, recursion.factorial(10))
        self.assertEquals(1307674368000, recursion.factorial(15))

        with self.assertRaises(ValueError):
            recursion.factorial(3/2)
        with self.assertRaises(ValueError):
            recursion.factorial(-4)

