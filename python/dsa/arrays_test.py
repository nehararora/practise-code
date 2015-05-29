"""
arrays_test.py: Test cases for array algorithm implementations.

"""

__author__ = 'nehar'

import unittest


from arrays import DynamicArray

# TODO: add ALL dynamic array operations (e.g. delete, insert etc)
class TestArrays(unittest.TestCase):

    def test_dynamic_array(self):
        """
        dynamic array tests.

        :return:
        """
        # test initial object properties.
        a = DynamicArray()
        self.assertIsNotNone(a)
        self.assertEquals(1, a._capacity)
        self.assertEquals(0, a._count)
        self.assertEquals(0, len(a))
        with self.assertRaises(IndexError):
            a[0]

        a.append(1)
        self.assertEquals(1, a._capacity)  # capacity unchanged
        self.assertEquals(1, a._count)  # count increases
        self.assertEquals(1, len(a))

        a.append(2)
        self.assertEquals(2, a._capacity)  # capacity doubles
        self.assertEquals(2, a._count)  # count increases
        self.assertEquals(2, len(a))

        a.append(3)
        self.assertEquals(4, a._capacity)  # capacity exceeded
        self.assertEquals(3, a._count)  # count increases
        self.assertEquals(3, len(a))

        a.append(4)
        self.assertEquals(4, a._capacity)  # unchanged
        self.assertEquals(4, a._count)  # count increases
        self.assertEquals(4, len(a))

        a.append(5)
        self.assertEquals(8, a._capacity)  # doubles
        self.assertEquals(5, a._count)  # count increases
        self.assertEquals(5, len(a))
