"""
set_disjointness_test.py: Test cases for the set disjointness algorithms
in set_disjointness.py.
"""

__author__ = 'nehar'

import unittest
from set_disjointness import SetDisjointness


class TestSetDisjointness(unittest.TestCase):
    """Demo test class"""

    def test_instance(self):
        """Test basic instantiation"""

        s = SetDisjointness([1], [2], [3])
        self.assertIsNotNone(s)
        self.assertEqual({1}, s.s1)
        self.assertEqual({2}, s.s2)
        self.assertEqual({3}, s.s3)

        with self.assertRaises(TypeError):
            SetDisjointness()

        with self.assertRaises(TypeError):
            SetDisjointness(1, 2, 3)

    def test_naive_disjoint(self):
        """
        Test naive 3-Way Set Disjointness implementation
        :return:
        """

        # the empty set is considered disjoint with itself.
        self.assertTrue(SetDisjointness([], [], []).naive_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], []).naive_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], [2]).naive_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2], [2], [1]).naive_is_disjoint())
        self.assertFalse(SetDisjointness([1], [1], [1]).naive_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2, 3, 4, 5, 6], [7, 8, 9, 0],
                                        [10, -1, 11, 12]).naive_is_disjoint())
        self.assertFalse(SetDisjointness([1, 2, 3, 4, 42, 6], [7, 8, 9, 42],
                                         [10, -1, 42, 12]).naive_is_disjoint())

    def test_short_circuit_disjoint(self):
        """
        Test short-circuited set Disjointness implementation
        :return:
        """

        self.assertTrue(SetDisjointness([], [], []).short_circuit_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], []).short_circuit_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], [2]).short_circuit_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2], [2], [1]).short_circuit_is_disjoint())
        self.assertFalse(SetDisjointness([1], [1], [1]).short_circuit_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2, 3, 4, 5, 6], [7, 8, 9, 0],
                                        [10, -1, 11, 12]).short_circuit_is_disjoint())
        self.assertFalse(SetDisjointness([1, 2, 3, 4, 42, 6], [7, 8, 9, 42],
                                         [10, -1, 42, 12]).short_circuit_is_disjoint())

    def test_sorting_disjoint(self):
        """
        Test Sorting based Set-Disjointness implementation
        :return:
        """
        self.assertTrue(SetDisjointness([], [], []).sorting_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], []).sorting_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], [2]).sorting_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2], [2], [1]).sorting_is_disjoint())
        self.assertFalse(SetDisjointness([1], [1], [1]).sorting_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2, 3, 4, 5, 6], [7, 8, 9, 0],
                                        [10, -1, 11, 12]).sorting_is_disjoint())
        self.assertFalse(SetDisjointness([1, 2, 3, 4, 42, 6], [7, 8, 9, 42],
                                         [10, -1, 42, 12]).sorting_is_disjoint())

    def test_map_disjoint(self):

        self.assertTrue(SetDisjointness([], [], []).map_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], []).map_is_disjoint())
        self.assertTrue(SetDisjointness([1], [1], [2]).map_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2], [2], [1]).map_is_disjoint())
        self.assertFalse(SetDisjointness([1], [1], [1]).map_is_disjoint())
        self.assertTrue(SetDisjointness([1, 2, 3, 4, 5, 6], [7, 8, 9, 0],
                                        [10, -1, 11, 12]).map_is_disjoint())
        self.assertFalse(SetDisjointness([1, 2, 3, 4, 42, 6], [7, 8, 9, 42],
                                         [10, -1, 42, 12]).map_is_disjoint())
