"""
arrays.py: Algorithms based on array operations.

Primarily from Chapter 5, Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'

import ctypes

class DynamicArray(object):
    """
    Dynamic Array class.

    Implements a dynamic array based on the low level ctypes array.
    Section 5.1.3, Data Structures and Algorithms in Python, Goodrich et al.
    """

    def __init__(self):
        """
        Create an empty array.
        :return:
        """
        # actual count
        self._count = 0
        self._capacity = 1

        # allocate capacity
        self._array = self._alloc(self._capacity)

    @staticmethod
    def _alloc(capacity):
        """
        Allocate array of specified capacity.
        :param capacity: capacity to allocate.
        :return: raw array
        """
        return (capacity * ctypes.py_object)()

    def __len__(self):
        """
        Return array length.

        :return:
        """
        return self._count

    def __getitem__(self, item):
        """
        Element access.

        :param item: index of element to access.
        :return: object at index item.
        """

        if not 0 <= item < self._count:
            raise IndexError("Invalid index")
        return self._array[item]


