"""
stacks.py: Stack based implementations.

refer: Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.
"""

__author__ = 'nehar'

from arrays import DynamicArray

class ArrayStack(object):
    """
    List (array) based stack implementation.
    """

    def __init__(self):
        """
        Initialize stack.
        """
        self._array = []

    def __len__(self):
        """
        Returns the size of the stack.

        :return: Number of elements in stack.
        """
        return len(self._array)

    def push(self, item):
        """
        Push an element onto the top of the stack.

        :param item: Element to place at top of stack.
        """
        self._array.append(item)

    def pop(self):
        """
        Remove and return the topmost element on stack.

        :return: Last inserted element.
        """
        if len(self._array) == 0:
            raise StackEmptyException
        return self._array.pop()

    def peek(self):
        """
        Examine (return) the top element without removing from stack.

        :return: Last inserted element.
        """
        if self.empty():
            raise StackEmptyException()

        return self._array[-1]

    def empty(self):
        """
        Checks whether stack is empty.

        :return: True if empty, false otherwise.
        """
        return True if len(self._array) == 0 else False


class DynamicArrayStack(object):
    """
    Custom DynamicArray based stack implementation.
    """

    def __init__(self):
        """
        Initialize stack.
        """
        self._array = DynamicArray()

    def __len__(self):
        """
        Returns the size of the stack.

        :return: Number of elements in stack.
        """
        return len(self._array)

    def push(self, item):
        """
        Push an element onto the top of the stack.

        :param item: Element to place at top of stack.
        """
        self._array.append(item)

    def pop(self):
        """
        Remove and return the topmost element on stack.

        :return: Last inserted element.
        """
        if len(self._array) == 0:
            raise StackEmptyException
        return self._array.pop()

    def peek(self):
        """
        Examine (return) the top element without removing from stack.

        :return: Last inserted element.
        """
        if self.empty():
            raise StackEmptyException()

        return self._array[-1]

    def empty(self):
        """
        Checks whether stack is empty.

        :return: True if empty, false otherwise.
        """
        return True if len(self._array) == 0 else False

class StackEmptyException(Exception):
    """
    Denote access to empty stack structure.
    """
    pass