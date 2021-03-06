"""
set_disjointness.py: Implementations of the Three-way Set Disjointedness.

The three-way set disjointness problem is defined as follows: Given three sets
of items, A, B, and C, they are three-way disjoint if there is no element
common to all three sets, ie, there exists no x such that x is in A, B, and C.

"""

__author__ = "nehar"

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
        O(n^3)
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

    def short_circuit_is_disjoint(self):
        """
        Short circuit third comparison on first mismatch.
        O(n^2) - since possible n matches.
        :return: None
        """
        for a in self.s1:
            for b in self.s2:
                # only compare to 3rd seq, if matched
                if a == b:
                    for c in self.s3:
                        if a == c:
                            # match!
                            return False
        return True

    def sorting_is_disjoint(self):
        """
        Sorting based solution.
        Since the 3 sequences are sets, merging and then sorting them should
        produce a run of 3 adjacent duplicates if they are not set-disjoint.
        o(n) to merge, o(nlogn) to sort, o(n) to determine dups so ~ o(nlogn)
        Note: python default sorting implementation: http://en.wikipedia.org/wiki/Timsort
        :return: None
        """
        # merge the sets
        s = list(self.s1) + list(self.s2) + list(self.s3)

        # sort them merged lists
        s = sorted(s)

        # check if adjacent elements are the same...
        for i in range(len(s)):
            try:
                if s[i] is s[i+1] is s[i+2]:
                    return False
            except IndexError:
                # handles the case when we run out of elements
                pass
        return True

    def map_is_disjoint(self):
        """
        Map based solution to 3 way set disjointness.
        totals up counts for each element in a map.
        o(n) since straight traversal through the lists
        and then o(1) map lookup.
        :return:
        """
        # merge the sets
        s = list(self.s1) + list(self.s2) + list(self.s3)
        counts = {}

        # count em up
        for element in s:
            counts[element] = counts.get(element, 0) + 1

        # since sets have unique items, count >3 for anything ==> bingo!
        for key in counts:
            if counts[key] >= 3:
                return False

        return True


if __name__ == "__main__":
    import set_disjointness_test
    suite = unittest.TestLoader().loadTestsFromModule(set_disjointness_test)
    unittest.TextTestRunner(verbosity=2).run(suite)
