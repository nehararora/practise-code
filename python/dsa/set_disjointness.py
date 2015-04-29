"""
set_disjointness.py: Implementations of the Three-way Set Disjointedness.

The three-way set disjointness problem is defined as follows: Given three sets
of items, A, B, and C, they are three-way disjoint if there is no element
common to all three sets, ie, there exists no x such that x is in A, B, and C.

Assume that A, B, and C are sets of items that can be ordered (integers); furthermore,
assume that it is possible to sort n integers in O(n log n) time. Give an O(n log n)
algorithm to decide whether the sets are three-way set disjoint.
"""

__auhor__ = "nehar"

import unittest


class SetDisjointness(object):
    """
    Demo class for Set Disjointness solutions.
    """
    def __init__(self, s1, s2, s3):
        """
        Initialize sets.
        For completes assumes sequence may not be sets.
        :param s1: Sequence 1
        :param s2: Sequence 2
        :param s3: Sequence 3
        :return:
        """
        self.s1 = frozenset(s1)
        self.s2 = frozenset(s2)
        self.s3 = frozenset(s3)

    def naive_is_disjoint(self):
        """
        Basic naive triple for loop implementation.
        Algorithm iterates over the three sets and compares
        every element to every other.
        :return: None
        """
        for a in self.s1:
            for b in self.s2:
                for c in self.s3:
                    if a == b == c:
                        # found a match - not disjoint!
                        return False

        # no match - sets are disjoint.
        return True
    # naive


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

        self.assertTrue(SetDisjointness([1], [1], [2]).naive_is_disjoint())

        self.assertFalse(SetDisjointness([1], [1], [1]).naive_is_disjoint())

        self.assertTrue(SetDisjointness([1, 2, 3, 4, 5, 6], [7, 8, 9, 0],
                                        [10, -1, 11, 12]).naive_is_disjoint())

        self.assertFalse(SetDisjointness([1, 2, 3, 4, 42, 6], [7, 8, 9, 42],
                                         [10, -1, 42, 12]).naive_is_disjoint())

if __name__ == "__main__":
    unittest.main()