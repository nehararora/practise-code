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
        # maximum elements the raw array can hold
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

        # array index out of bounds
        if not 0 <= item < self._count:
            raise IndexError("Invalid index")

        return self._array[item]

    def append(self, item):
        """
        Add element to end of array.
        Array is doubled on attempt to append beyond capacity.

        :param item: Element to append
        :return: None
        """
        print(self._count)
        # resize
        if self._count == self._capacity:
            self._resize(2 * self._capacity)

        # append element
        self._array[self._count] = item

        self._count += 1

    def _resize(self, capacity):
        """
        Resize backing array to capacity.

        :param capacity:
        :return:
        """
        # make a new array
        new_array = self._alloc(capacity)

        # copy existing elements over
        for i, item in enumerate(self._array):
            new_array[i] = item

        # replace old array
        self._array = new_array
        self._capacity = capacity