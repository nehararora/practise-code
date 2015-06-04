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