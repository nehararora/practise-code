"""
sorting.py: Implementation of various sorting algorithms.

Primarily from Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'

class Sorting(object):
    """
    Various sorting implementations.
    """

    @staticmethod
    def insertion_sort(a=[]):
        """
        Insertion sort implementation.
        Works by inserting each element in the unsorted portion of the array,
        at the appropriate location within the sorted portion.

        o(n^2) worst case: the double for loop causes a full quadratic scan when
        the array is sorted in reverse order. Best case is o(n) if the array is
        close to perfectly sorted.

        Note: Implementation modifies input array state.
        
        Section 5.5.2, Data Structures and Algorithms in Python, Goodrich et al.
        """

        for i in range(1, len(a)):
            # insert current element into correct position within sorted portion.
            curr = a[i]
            j = i
            while j > 0 and a[j-1] > curr:
                a[j] = a[j-1]
                j -= 1
            a[j] = curr

        return a
