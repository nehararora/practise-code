"""
arrays_test.py: Test cases for array algorithm implementations.

"""

__author__ = 'nehar'

import unittest

from arrays import DynamicArray
from arrays import CaesarCipher
from arrays import MultiDimensional
from arrays import NaturalJoin


class TestDynamicArray(unittest.TestCase):
    """
    Test cases for DynamicArray implementation.
    """

    def test_dynamic_array(self):
        """
        dynamic array tests.

        """
        # test initial object properties.
        a = DynamicArray()
        self.assertIsNotNone(a)
        self.assertEquals(1, a._capacity)
        self.assertEquals(0, a._count)
        self.assertEquals(0, len(a))
        with self.assertRaises(IndexError):
            a[0]

    def test_append(self):
        """
        Test DynamicArray append.

        """
        # test some appends...
        a = DynamicArray()
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

    def test_insert(self):
        """
        Test DynamicArray insert.

        """
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

    def test_remove(self):
        """
        Test DynamicArray remove.
        """
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
        self.assertEquals(4, c._capacity)
        self.assertEquals(2, c._count)
        self.assertEquals(2, len(c))
        self.assertEquals([3, 4], [x for x in c])

        c.remove(3)
        self.assertEquals(2, c._capacity)
        self.assertEquals(1, c._count)
        self.assertEquals(1, len(c))
        self.assertEquals([4], [x for x in c])

        c.remove(4)
        self.assertEquals(2, c._capacity)
        self.assertEquals(0, c._count)
        self.assertEquals(0, len(c))
        self.assertEquals([], [x for x in c])

        with self.assertRaises(ValueError):
            c.remove(4)

    def test_remove_all(self):
        """
        Test DynamicArray remove.
        """
        # test remove
        c = DynamicArray()
        c.append(1)
        c.append(2)
        c.append(3)
        c.append(4)
        c.append(5)
        c.append(4)

        c.remove_all(1)
        self.assertEquals(8, c._capacity)
        self.assertEquals(5, c._count)
        self.assertEquals(5, len(c))
        self.assertEquals([2, 3, 4, 5, 4], [x for x in c])

        c.remove_all(5)
        self.assertEquals(8, c._capacity)
        self.assertEquals(4, c._count)
        self.assertEquals(4, len(c))
        self.assertEquals([2, 3, 4, 4], [x for x in c])

        c.remove_all(2)
        self.assertEquals(8, c._capacity)
        self.assertEquals(3, c._count)
        self.assertEquals(3, len(c))
        self.assertEquals([3, 4, 4], [x for x in c])

        c.remove_all(3)
        self.assertEquals(4, c._capacity)
        self.assertEquals(2, c._count)
        self.assertEquals(2, len(c))
        self.assertEquals([4, 4], [x for x in c])

        c.remove_all(4)
        self.assertEquals(2, c._capacity)
        self.assertEquals(0, c._count)
        self.assertEquals(0, len(c))
        self.assertEquals([], [x for x in c])

        with self.assertRaises(ValueError):
            c.remove_all(4)

    def test_pop(self):
        """
        Test DynamicArray pop.
        """
        # test pop
        c = DynamicArray()
        c.append(1)
        c.append(2)
        # try an object
        c.append([1, 2])
        c.append(4)
        c.append(5)

        c.pop()
        self.assertEquals(8, c._capacity)
        self.assertEquals(4, c._count)
        self.assertEquals(4, len(c))
        self.assertEquals([1, 2, [1, 2], 4], [x for x in c])

        c.pop()
        self.assertEquals(8, c._capacity)
        self.assertEquals(3, c._count)
        self.assertEquals(3, len(c))
        self.assertEquals([1, 2, [1, 2]], [x for x in c])

        c.pop()
        self.assertEquals(4, c._capacity)
        self.assertEquals(2, c._count)
        self.assertEquals(2, len(c))
        self.assertEquals([1, 2], [x for x in c])

        c.pop()
        self.assertEquals(2, c._capacity)
        self.assertEquals(1, c._count)
        self.assertEquals(1, len(c))
        self.assertEquals([1], [x for x in c])

        c.pop()
        self.assertEquals(2, c._capacity)
        self.assertEquals(0, c._count)
        self.assertEquals(0, len(c))
        self.assertEquals([], [x for x in c])

        with self.assertRaises(ValueError):
            c.pop()

    def test_negative_indexing(self):
        """
        Test negative index element access.
        """
        c = DynamicArray()
        c.append(1)
        c.append(2)
        c.append(3)
        c.append(4)
        c.append(5)
        self.assertEquals(5, c[-1])
        self.assertEquals(4, c[-2])
        self.assertEquals(3, c[-3])
        self.assertEquals(2, c[-4])
        self.assertEquals(1, c[-5])
        with self.assertRaises(IndexError):
            c[-6]

class TestCaesarCipher(unittest.TestCase):
    """
    Test cases for the CaeserCipher implementation.
    """
    def test_instantiation(self):
        """
        Test basic object creation.
        """
        c = CaesarCipher(0)
        self.assertIsNotNone(c)
        self.assertEquals(0, c._shift)
        self.assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZ", c._enc_key)
        self.assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZ", c._dec_key)

    def test_rot13(self):
        """
        Basic encryption test using rot13.
        """

        # rot-13 - same backwards and forwards
        c = CaesarCipher(13)
        self.assertEquals("NOPQRSTUVWXYZABCDEFGHIJKLM", c._enc_key)
        self.assertEquals("NOPQRSTUVWXYZABCDEFGHIJKLM", c._dec_key)
        self.assertEquals("URYYB", c.encrypt("HELLO"))
        self.assertEquals("URYYB", c.encrypt("hello"))
        self.assertEquals("URYYB FRPERG ZRFFNTR ERPVCVRAG",
                          c.encrypt("hello secret message recipient"))

    def test_enc_dec(self):
        """
        Test some encryption and decryption cases.

        :return:
        """
        c = CaesarCipher(13)
        self.assertEquals("NOPQRSTUVWXYZABCDEFGHIJKLM", c._enc_key)
        self.assertEquals("NOPQRSTUVWXYZABCDEFGHIJKLM", c._dec_key)
        self.assertEquals("TEST MESSAGE", c.decrypt(c.encrypt("Test Message")))

        c = CaesarCipher(0)
        self.assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZ", c._enc_key)
        self.assertEquals("ABCDEFGHIJKLMNOPQRSTUVWXYZ", c._dec_key)
        self.assertEquals("TEST MESSAGE", c.encrypt("Test Message"))
        self.assertEquals("TEST MESSAGE", c.decrypt(c.encrypt("Test Message")))

        c = CaesarCipher(1)
        self.assertEquals("BCDEFGHIJKLMNOPQRSTUVWXYZA", c._enc_key)
        self.assertEquals("ZABCDEFGHIJKLMNOPQRSTUVWXY", c._dec_key)
        self.assertEquals("UFTU NFTTBHF", c.encrypt("Test Message"))
        self.assertEquals("TEST MESSAGE", c.decrypt("UFTU NFTTBHF"))

        c = CaesarCipher(3)
        self.assertEquals("WKH HDJOH LV LQ SODB; PHHW DW MRH'V.",
                          c.encrypt("THE EAGLE IS IN PLAY; MEET AT JOE'S."))


class TestMultiDimensional(unittest.TestCase):
    """
    Test cases for multi dimensional array implementation.
    """
    def test_instantiation(self):
        """
        Test object creation.

        """

        m = MultiDimensional(row=1, col=1)
        self.assertEquals(1, m._row)
        self.assertEquals(1, m._col)
        self.assertEquals([[1]], m._data)

        m = MultiDimensional(row=1, col=2, value=2)
        self.assertEquals([[2, 2]], m._data)

        m = MultiDimensional(2, 5, value=42)
        self.assertEquals([[42, 42, 42, 42, 42],
                           [42, 42, 42, 42, 42]], m._data)

    def test_compute_sum_std(self):
        """
        Test standard control structure based compute sum.
        """

        m = MultiDimensional(row=0, col=0)
        self.assertEquals(0, m.compute_sum_std())

        m = MultiDimensional(row=1, col=1)
        self.assertEquals(1, m.compute_sum_std())

        m = MultiDimensional(row=1, col=2, value=2)
        self.assertEquals(4, m.compute_sum_std())

        m = MultiDimensional(row=2, col=5, value=42)
        self.assertEquals(42*5*2, m.compute_sum_std())

    def test_compute(self):
        """
        Test comprehension based compute sum.
        """

        m = MultiDimensional(row=0, col=0)
        self.assertEquals(0, m.compute_sum())

        m = MultiDimensional(row=1, col=2)
        self.assertEquals(2, m.compute_sum())

        m = MultiDimensional(row=1, col=2, value=2)
        self.assertEquals(4, m.compute_sum())

        m = MultiDimensional(row=2, col=5, value=42)
        self.assertEquals(42*5*2, m.compute_sum())

class TestNaturalJoin(unittest.TestCase):
    """
    Test cases for join implementations.
    """

    def test_naive_join(self):
        """
        Naive natural join test cases.
        """
        n = NaturalJoin()
        self.assertEqual([], n.naive(list1=[], list2=[]))

        self.assertEqual([], n.naive(list1=[(1, 2)], list2=[(3, 4)]))

        list1 = [(2, 1), (3, 1), (3, 3)]
        list2 = [(3, 3), (1, 4), (5, 2), (3, 1)]
        expected = [(2, 1, 4), (3, 1, 4), (3, 3, 3), (3, 3, 1)]
        self.assertEqual(expected, n.naive(list1=list1, list2=list2))

        list1 = [(1, 2), (3, 2), (4, 2)]
        list2 = [(2, 5), (2, 6), (2, 7)]
        expected = [(1, 2, 5), (1, 2, 6), (1, 2, 7),
                    (3, 2, 5), (3, 2, 6), (3, 2, 7),
                    (4, 2, 5), (4, 2, 6), (4, 2, 7)]
        self.assertEqual(expected, n.naive(list1, list2))

    def test_sort_merge_join(self):
        """
        Tests the sort merge join implementation.
        """

        n = NaturalJoin()
        self.assertEqual([], n.sort_merge(list1=[], list2=[]))

        self.assertEqual([], n.naive(list1=[(1, 2)], list2=[(3, 4)]))

        list1 = [(2, 1), (3, 1), (3, 3)]
        list2 = [(3, 3), (1, 4), (5, 2), (3, 1)]
        expected = [(2, 1, 4), (3, 1, 4), (3, 3, 3), (3, 3, 1)]
        # self.assertEqual(expected, n.sort_merge(list1=list1, list2=list2))

        list1 = [(1, 2), (3, 2), (4, 2)]
        list2 = [(2, 5), (2, 6), (2, 7)]
        expected = [(1, 2, 5), (1, 2, 6), (1, 2, 7),
                    (3, 2, 5), (3, 2, 6), (3, 2, 7),
                    (4, 2, 5), (4, 2, 6), (4, 2, 7)]
        # self.assertEqual(expected, n.sort_merge(list1, list2))
