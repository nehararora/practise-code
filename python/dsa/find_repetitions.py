"""
find_repetitions.py: Implementation of find repetitions in a sequence
algorithms.
"""

__author__ = 'nehar'


class FindRepetitions(object):

    def __init__(self, seq):
        self.s = seq

    def find_duplicates(self):
        """
        Find and return all duplicates in input list.

        :return: List of duplicate entries.
        """
        counts = dict()
        for a in self.s:
            counts[a] = counts.get(a, 0) + 1

        return {key for key in counts if counts[key] > 1}

    def find_max_repetitions(self):
        """
        A sequence S contains n integers taken from the interval [0, 4n], with
        repetitions allowed. Describe an efficient algorithm for determining an
        integer value k that occurs the most often in S. What is the running
        time of your algorithm?

        exercise 3.54, Chapter 3, Data Structures and Algorithms in Python,
        Goodrich et al.
        ~ O(n)
        :return:
        """

        # maintain counts in a dictionary
        counts = dict()

        # o(log(n))
        for a in self.s:
            counts[a] = counts.get(a, 0) + 1

        # find the key with the maximum count
        max_key = None
        max_count = 0

        for key in counts:
            if max_count < counts[key]:
                max_count = counts[key]
                max_key = key

        return max_key
