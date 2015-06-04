"""
prefix_averages.py: Implementations of various Prefix Averages algorithms.

The prefix averages problem is defined as follows: Given a sequence S
consisting of n numbers, compute a sequence A such that A[i] is the average
of elements S[0], ... S[i] for i=0, ..., n-1, that is,
A[i] ==  (S[0] + ... + S[i])/(i+1)

"""

__author__ = 'nehar'

import unittest


class PrefixAverages(object):
    """
    Prefix averages implementation.
    """
    def __init__(self, s=[]):
        self.s = s

        # allowing lists only for now.
        if type(s) is not list:
            raise TypeError

    def naive(self):
        """
        Naive implementation of prefix average calculation.

        :return: new sequence containing prefix averages.
        """

        a = [0] * len(self.s)
        for j in range(len(self.s)):
            total = 0
            for i in range(j+1):
                total += self.s[i]
            a[j] = round(float(total)/(j+1), 2)
        return a

    def linear(self):
        """
        Linear time implementation - uses prior computations
        for total instead of anew every-time.

        :return: new sequence containing prefix averages.
        """
        a = [0] * len(self.s)
        total = 0
        for i in range(len(self.s)):
            total += self.s[i]
            a[i] = round(float(total)/(i+1), 2)
        return a


# TODO: move to test module
class TestPrefixAverages(unittest.TestCase):
    """
    Test cases for prefix averages implementations.

    """
    def test_instance(self):
        """Test basic instantiation"""

        p = PrefixAverages()
        self.assertIsNotNone(p)
        self.assertEqual(p.s, [])

        p = PrefixAverages([1, 2, 3])
        self.assertIsNotNone(p)
        self.assertEqual(p.s, [1, 2, 3])

        with self.assertRaises(TypeError):
            PrefixAverages("Foobar")
        with self.assertRaises(TypeError):
            PrefixAverages((1, 2, 3))

    def test_naive_prefix_average(self):

        self.assertEqual([], PrefixAverages().naive())
        self.assertEqual([7.0, 5.0, 3.0, 2.75, 4.0, 3.33, 2.97, 9.1, 8.33, 97.5],
                         PrefixAverages([7, 3, -1, 2, 9,
                                         0, 0.8, 52, 2.2, 900]).naive())

        self.assertEqual([1, 1.5, 2, 2.5], PrefixAverages([1, 2, 3, 4]).naive())

    def test_linear_prefix_average(self):

        self.assertEqual([], PrefixAverages().linear())
        self.assertEqual([7.0, 5.0, 3.0, 2.75, 4.0, 3.33, 2.97, 9.1, 8.33, 97.5],
                         PrefixAverages([7, 3, -1, 2, 9,
                                         0, 0.8, 52, 2.2, 900]).linear())

        self.assertEqual([1, 1.5, 2, 2.5], PrefixAverages([1, 2, 3, 4]).linear())
