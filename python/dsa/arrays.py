"""
arrays.py: Algorithms based on array operations.

Primarily from Chapter 5, Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'


class DynamicArray(object):
    """
    Dynamic Array class.

    Implements a dynamic array based on the low level ctypes array.
    Section 5.1.3, Data Structures and Algorithms in Python, Goodrich et al.
    """

    def __init__(self):
        """
        Initialize the array object.
        :return:
        """