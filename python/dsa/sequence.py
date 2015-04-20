"""
sequence.py: Illustrates Progressions.
ArithmeticProgression: Arithmetic progression iterator.
GeometricProgression:
FibonacciProgression:

"""

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
        using the formual an = a1 + (n-1)*d
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
        print("{} {} {}".format(self.count, self.start, self._get_nth(self.count)))
        return (self.count * (self.start + self._get_nth(self.count))) / 2


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
        print([x for x in ArithmeticProgression(count=10, start=100, diff=100)])


class GeometricProgression(object):
    """
    Geometric Progression: In the simplest form acts as a GP iterator.
    """
    def __init__(self, count, start=1, base=1):
        """
        Initialize
        :param count:
        :param start:
        :param base:
        :return:
        """

    def __iter__(self):
        """
        """
        return self
    def __next__(self):
        """
        """
        return None
    def next(self):
        """
        """
        return None

class GeometricProgressionTest(unittest.TestCase):
    """
    Geometric progression test class.
    """
    def test_generator(self):
        self.assertTrue(GeometricProgression(10) is not None)
        self.assertEqual(None, [x for x in GeometricProgression(10)])



if __name__ == '__main__':
    unittest.main()