"""
recursion_test.py: Test cases for recursion algorithms.
"""

__author__ = 'nehar'

import unittest
from recursion import factorial
from recursion import Ruler
from recursion import binary_search
from recursion import recursive_sum
from recursion import recursive_reverse
from recursion import naive_power


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
        x = "---- 0\n-\n--\n-\n---\n-\n--\n-\n---- 1\n-\n--\n-\n---\n-\n--\n-\n---- 2\n"
        self.assertEquals(x, Ruler(inches=2, major_length=4).draw())
        print("\n\n"*5)

        x = "----- 0\n-\n--\n-\n---\n-\n--\n-\n----\n-\n--\n-\n---\n-\n--\n-\n----- 1\n"
        self.assertEquals(x, Ruler(inches=1, major_length=5).draw())
        print("\n\n"*5)

        x = """--- 0\n-\n--\n-\n--- 1\n-\n--\n-\n--- 2\n-\n--\n-\n--- 3\n"""
        self.assertEqual(x, Ruler(inches=3, major_length=3).draw())

    def test_binary_search(self):
        """
        Test recursive Binary search.
        :return:
        """
        binary_search([1, 2, 3, 4, 5], 5, 0, 4)

    def test_recursive_sum(self):
        """
        Test Linear recursive sum of sequence.

        :return:
        """
        self.assertEquals(0, recursive_sum())
        self.assertEquals(0, recursive_sum([]))
        self.assertEquals(1, recursive_sum([1]))
        self.assertEquals(3, recursive_sum([1, 2]))
        self.assertEquals(6, recursive_sum([1, 2, 3]))

    def test_recursive_reverse(self):
        """
        Test linear recursion based reverse.

        :return:
        """
        self.assertEquals([], recursive_reverse())
        self.assertEquals([1], recursive_reverse([1]))
        self.assertEquals([2, 1], recursive_reverse([1, 2]))
        self.assertEquals([3, 2, 1], recursive_reverse([1, 2, 3]))
        self.assertEquals([8, 7, 6, 5, 4, 3, 2, 1],
                          recursive_reverse([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEquals([5, 9, 8, 2, 6, 3, 4],
                          recursive_reverse([4, 3, 6, 2, 8, 9, 5]))

    def test_naive_power(self):
        """
        Test naive recursive power function implementation.
        :return:
        """
        self.assertEquals(1, naive_power(2, 0))
        self.assertEquals(2, naive_power(2, 1))
        self.assertEquals(4, naive_power(2, 2))
        self.assertEquals(-1, naive_power(-1, 1))
        self.assertEquals(27, naive_power(3, 3))
        self.assertEquals(-27, naive_power(-3, 3))
