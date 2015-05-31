"""
sequence.py: Illustrates Progressions.
"""

__author__ = "nehar"

import unittest


class ArithmeticProgression(object):
    """
    Arithmetic Progression class: In it's simplest form acts as an AP iterator.
    """

    def __init__(self, count, start=1, diff=1):
        """
        """
        self.start = start
        self._current = 0
        self.count = count
        self.delta = diff

    def __iter__(self):
        return self

    def _get_nth(self, n):
        """
        returns the n'th element in the progression.
        """
        return self.start + ((n - 1) * self.delta)

    def next(self):
        """
        Returns the next element of the progression
        using the formula an = a1 + (n-1)*d
        """
        if self._current is self.count:
            raise StopIteration

        self._current += 1
        return self._get_nth(self._current)

    def __next__(self):
        """
        Support for python 3.
        """
        return self.next()

    def sum(self):
        """
        """
        return (self.count * (self.start + self._get_nth(self.count))) / 2


class GeometricProgression(object):
    """
    Geometric Progression: In the simplest form acts as a GP iterator.
    """
    def __init__(self, count, scale_factor=1, common_ratio=1):
        """
        Initialize
        :param count:
        :param scale_factor:
        :param common_ratio:
        :return:
        """
        assert common_ratio is not 0, "Common Ration cannot be null"

        self.count = count
        self._current = 0
        self.a = scale_factor
        self.r = common_ratio

    def __iter__(self):
        """
        """
        return self

    def _get_nth(self, n):
        """
        :param n:
        :return:
        """
        return self.a * (self.r ** (n-1))

    def __next__(self):
        """
        Python 3 support.
        """
        return self.next()

    def next(self):
        """
        Return the next element of the progression
        using the formula an = a(r^(n-1))
        """
        if self._current is self.count:
            raise StopIteration

        self._current += 1

        return self._get_nth(self._current)

    def mean(self):
        """
        Geometric mean of specified elements.
        :return: Geometric mean
        """

    def sum(self):
        """
        Produces the summation of the sequence.
        using the formula a*(1- (r^m)) / (1-r) where a
        is the first term, and m the number of terms.
        """
        return self.a * (1-(self.r ** self.count))/(1-self.r)


class FibonacciProgression(object):
    """
    Fibonacci Iterator.
    """
    def __init__(self, count, first=0, second=1):
        """
        Initialize the progression.

        :param first:
        :param second:
        :return:
        """
        self.count = count
        self._current = 0
        # need to set first and second to initial element.
        self.first = first
        self.second = second

    def __iter__(self):
        return self

    def __next__(self):
        """Python 3 support"""
        return self.next()

    def next(self):
        if self._current is self.count:
            raise StopIteration
        value = self.first
        self.first, self.second = self.second, self.first + self.second
        self._current += 1
        return value


class FindMissingNumber(object):
    """
    Algorithms to find missing number given sequence in the range 0-n.

    A sequence S contains n - 1 unique integers in the range [0, n - 1], that
    is, there is one number from this range that is not in S. Design an O(n)-
    time algorithm for finding that number. You are only allowed to use O(1)
    additional space besides the sequence S itself.

    Exercise C-3.45, Chapter 3, Data Structures and Algorithms in Python.
    """
    def __init__(self):
        pass

    @staticmethod
    def naive_find_missing(seq):
        """
        Naive implementation for finding the missing number.
        linear time algorithm.
        """
        for i, num in enumerate(seq):
            if i is not num:
                return i

        # if nothing missing, return None
        return None

    @staticmethod
    def summation_find_missing(seq):
        """
        Implementation based on sum of n numbers.
        O(n( - note that the builtin len() is constant time.
        """
        n = seq[len(seq) - 1]

        summation = n * (n+1)/2
        total = 0
        for i in seq:
            total += i

        return summation - total

if __name__ == '__main__':
    import sequence_test
    suite = unittest.TestLoader().loadTestsFromModule(sequence_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
