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

        # test some appends...
        a.append(1)
        self.assertEquals(1, a._capacity)  # capacity unchanged
        self.assertEquals(1, a._count)  # count increases
        self.assertEquals(1, len(a))
        self.assertEquals([1], [x for x in a])

        a.append(2)
        self.assertEquals(2, a._capacity)  # capacity doubles
        self.assertEquals(2, a._count)  # count increases
        self.assertEquals(2, len(a))
        self.assertEquals([1, 2], [x for x in a])

        a.append(3)
        self.assertEquals(4, a._capacity)  # capacity exceeded
        self.assertEquals(3, a._count)  # count increases
        self.assertEquals(3, len(a))
        self.assertEquals([1, 2, 3], [x for x in a])

        a.append(4)
        self.assertEquals(4, a._capacity)  # unchanged
        self.assertEquals(4, a._count)  # count increases
        self.assertEquals(4, len(a))
        self.assertEquals([1, 2, 3, 4], [x for x in a])

        a.append(5)
        self.assertEquals(8, a._capacity)  # doubles
        self.assertEquals(5, a._count)  # count increases
        self.assertEquals(5, len(a))
        self.assertEquals([1, 2, 3, 4, 5], [x for x in a])

        # try some inserts...
        b = DynamicArray()

        b.insert(0, 2)
        self.assertEquals(1, b._capacity)  # capacity unchanged
        self.assertEquals(1, b._count)  # count increases
        self.assertEquals(1, len(b))
        self.assertEquals([2], [x for x in b])

        b.insert(1, 4)
        self.assertEquals(2, b._capacity)  # capacity unchanged
        self.assertEquals(2, b._count)  # count increases
        self.assertEquals(2, len(b))
        self.assertEquals([2, 4], [x for x in b])
        print(b)
        b.insert(1, 3)
        self.assertEquals(4, b._capacity)  # capacity unchanged
        self.assertEquals(3, b._count)  # count increases
        self.assertEquals(3, len(b))
        self.assertEquals([2, 3, 4], [x for x in b])

        b.insert(0, 1)
        self.assertEquals(4, b._capacity)  # capacity unchanged
        self.assertEquals(4, b._count)  # count increases
        self.assertEquals(4, len(b))
        self.assertEquals([1, 2, 3, 4], [x for x in b])

        b.insert(4, 5)
        self.assertEquals(8, b._capacity)  # capacity unchanged
        self.assertEquals(5, b._count)  # count increases
        self.assertEquals(5, len(b))
        self.assertEquals([1, 2, 3, 4, 5], [x for x in b])

        # test remove
        c = DynamicArray()
        c.append(1)
        c.append(2)
        c.append(3)
        c.append(4)
        c.append(5)

        c.remove(1)
        self.assertEquals(8, c._capacity)
        self.assertEquals(4, c._count)
        self.assertEquals(4, len(c))
        self.assertEquals([2, 3, 4, 5], [x for x in c])

        c.remove(5)
        self.assertEquals(8, c._capacity)
        self.assertEquals(3, c._count)
        self.assertEquals(3, len(c))
        self.assertEquals([2, 3, 4], [x for x in c])

        c.remove(2)
        self.assertEquals(8, c._capacity)
        self.assertEquals(2, c._count)
        self.assertEquals(2, len(c))
        self.assertEquals([3, 4], [x for x in c])

        c.remove(3)
        self.assertEquals(8, c._capacity)
        self.assertEquals(1, c._count)
        self.assertEquals(1, len(c))
        self.assertEquals([4], [x for x in c])

        c.remove(4)
        self.assertEquals(8, c._capacity)
        self.assertEquals(0, c._count)
        self.assertEquals(0, len(c))
        self.assertEquals([], [x for x in c])

        with self.assertRaises(ValueError):
            c.remove(4)

