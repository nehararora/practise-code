"""
arrays_test.py: Test cases for array algorithm implementations.

"""

__author__ = 'nehar'

import unittest

from arrays import DynamicArray

class TestArrays(unittest.TestCase):

    def test_dynamic_array(self):
        """
        dynamic array tests.

        :return:
        """
        a = DynamicArray()
        self.assertIsNotNone(a)
