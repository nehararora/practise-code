"""
sorting_tests.py: Test cases for sorting algorithm implementations.

"""

__author__ = 'nehar'

import unittest

from sorting import Sorting

class TestSorting(unittest.TestCase):
    """
    Sorting test cases.

    """

    def test_insertion_sort(self):
        """

        :return:
        """
        s = Sorting()

        self.assertEqual([], s.insertion_sort([]))
        self.assertEqual([1], s.insertion_sort([1]))
        self.assertEqual([1, 2, 3], s.insertion_sort([3, 2, 1]))
        self.assertEqual([-12, -1, 3], s.insertion_sort([3, -1, -12]))
