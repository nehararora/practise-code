"""
sequence_test.py: Test cases for the sequence algorithms in sequence.py.
"""

__author__ = 'nehar'

import unittest
import random

from sequence import ArithmeticProgression
from sequence import GeometricProgression
from sequence import FibonacciProgression
from sequence import FindMissingNumber


class TestArithmeticProgression(unittest.TestCase):
    """
    Arithmetic Progression test class.
    """
    def test_generator(self):
        self.assertTrue(ArithmeticProgression(10) is not None)
        self.assertEqual([1, 2, 3, 4, 5], [x for x in ArithmeticProgression(5)])

    def test_sequences(self):
        self.assertEqual([x for x in ArithmeticProgression(100)], [x for x in range(1, 101)])

    def test_sum(self):
        self.assertEqual(5050, ArithmeticProgression(100).sum())
        self.assertEqual(55, ArithmeticProgression(10).sum())

    def test_last(self):
        self.assertEqual(10, ArithmeticProgression(10)._get_nth(10))
        self.assertEqual(1000, ArithmeticProgression(count=10, start=100, diff=100)._get_nth(10))


class TestGeometricProgression(unittest.TestCase):
    """
    Geometric progression test class.
    """
    def test_generator(self):

        with self.assertRaises(AssertionError):
            GeometricProgression(2, common_ratio=0)

        self.assertTrue(GeometricProgression(10) is not None)
        self.assertEqual([1, 1, 1, 1, 1], [x for x in GeometricProgression(5)])

    def test_sequence(self):
        """
        verify a couple of known sequences.
        """
        self.assertEqual([1, -3, 9, -27, 81, -243],
                         [x for x in GeometricProgression(6, 1, -3)])

        self.assertEqual([1, 1, 1, 1, 1],
                         [x for x in GeometricProgression(5, 1, 1)])

        self.assertEqual([4, 40, 400, 4000, 40000],
                         [x for x in GeometricProgression(5, 4, 10)])

        # TODO: need to fix for floating point math
        # self.assertEqual([9, 3, round(1/3, 5), round(1/9, 5)],
        #                 [x for x in GeometricProgression(5, 9, round(1/3, 5))])

    def test_sum(self):
        with self.assertRaises(ZeroDivisionError):
            GeometricProgression(1, 1, 1).sum()

        self.assertEqual(312, GeometricProgression(4, 2, 5).sum())
        self.assertEqual(2097150, GeometricProgression(20, -6, -2).sum())
        self.assertEqual(416.622976, GeometricProgression(10, 250, .4).sum())


class TestFibonacciProgression(unittest.TestCase):
    """
    Fibonacci sequence test class.
    """
    def test_generator(self):
        self.assertTrue(FibonacciProgression(1) is not None)
        self.assertTrue(FibonacciProgression(1, 2, 3) is not None)

    def test_sequence(self):
        self.assertEqual([0, 1, 1, 2, 3], [x for x in FibonacciProgression(5)])
        self.assertEqual([-1, 0, -1, -1, -2, -3], [x for x in FibonacciProgression(6, -1, 0)])


class TestFindMissingNumber(unittest.TestCase):
    def test_instance(self):
        """
        Test object instantiation.
        """

        self.assertIsNotNone(FindMissingNumber())

        with self.assertRaises(TypeError):
            FindMissingNumber().naive_find_missing()

    def test_naive_find_missing(self):

        f = FindMissingNumber()
        n = 100
        s = [x for x in range(n)]

        expected = random.randint(0, n)

        # remove an random element...
        s.remove(expected)

        actual = f.naive_find_missing(s)
        self.assertEqual(expected, actual)

    def test_summation_find_missing(self):

        f = FindMissingNumber()
        n = 100
        s = [x for x in range(n)]
        expected = random.randint(0, n)

        # remove an random element...
        s.remove(expected)

        actual = f.summation_find_missing(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()