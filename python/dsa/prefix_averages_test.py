"""
prefix_averages_tests.py: Test cases for the prefix averages implementation.
"""

__author__ = 'nehar'

import unittest
from prefix_averages import PrefixAverages


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
