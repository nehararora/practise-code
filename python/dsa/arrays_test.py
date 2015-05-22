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
        # test basic object properties.
        a = DynamicArray()
        self.assertIsNotNone(a)
        self.assertEquals(1, a._capacity)
        self.assertEquals(0, a._count)
        self.assertEquals(0, len(a))
        with self.assertRaises(IndexError):
            a[0]

