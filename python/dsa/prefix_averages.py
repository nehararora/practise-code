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
    def __init__(self, s=[]):
        self.s = s

        # allowing lists only for now.
        if type(s) is not list:
            raise TypeError

    def naive_prefix_average(self):
        """
        Naive implementation of prefix average calculation.

        :return: new sequence containing prefix averages.
        """

        a = [0] * len(self.s)
        for j in range(len(self.s)):
            total = 0
            for i in range(j+1):
                total += self.s[i]
            a[j] = float(total)/(j+1)
            print(a[j])
        return a


class TestPrefixAverages(unittest.TestCase):
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

        self.assertEqual([], PrefixAverages().naive_prefix_average())
        self.assertEqual([7.0, 5.0, 3.0, 2.75, 4.0, 3.33], PrefixAverages(
            [7, 3, -1, 2, 9, 0, 0.8, 52, 2.2, 900]).naive_prefix_average())
        self.assertEqual([],
            PrefixAverages([12, 14, 13, 15, 19, 17, 16, 11, 18, 20]).naive_prefix_average())
