"""
find_repetitions_test.py: Test cases for the find repetitions algorithms.
"""
__author__ = 'nehar'

import unittest
from find_repetitions import FindRepetitions


class TestFindRepetitions(unittest.TestCase):

    def test_instance(self):
        with self.assertRaises(TypeError):
            FindRepetitions()
        f = FindRepetitions([1, 2, 3])
        self.assertIsNotNone(f)
        self.assertEquals([1, 2, 3], f.s)

    def test_find_max_repetitions(self):
        f = FindRepetitions([1, 2, 3, 4, 1, 3, 3, 10, 10, 10, 10])
        self.assertEquals(10, f.find_max_repetitions())

        self.assertEquals(None, FindRepetitions([]).find_max_repetitions())
