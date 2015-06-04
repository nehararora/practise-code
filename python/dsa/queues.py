"""
queues.py: Queue data structure implementations.

refer: Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'


class ArrayQueue(object):
    """
    Array/List based queue.

    Using a plain array will cause O(n) operations on either the dequeue or
    the enqueue since elements need to get shifted, so we use circular array.
    """

    ARRAY_SIZE = 5

    def __init__(self):
        """
        Initialize queue.
        """
        self._array = [None] * ArrayQueue.ARRAY_SIZE

        # track the start and length
        self._head = 0
        self._len = 0

    def __len__(self):
        """
        Return length of the data structure.

        :return: Number of elements in queue.
        """
        return self._len

    def enqueue(self, element):
        """
        Append element to end of queue.

        will resize on overflow.

        :param element: element to append.
        """
        # resize on overflow
        if self._len == len(self._array):
            pass
        # next open slot is len elements away from front...
        i = (self._head + self._len) % len(self._array)

        # enqueue and increment count
        self._array[i] = element
        self._len += 1

    def dequeue(self):
        """
        Remove and return element at front of queue.

        :return: First element in queue.
        """
        if self.empty():
            raise QueueEmptyException()
        data = self._array[self._head]
        # move "pointer" to new head
        self._head = (self._head + 1) % len(self._array)
        self._len -= 1
        return data

    def first(self):
        """
        Returns the element at front of queue without removing.

        :return: First element in queue.
        """
        if self.empty():
            raise QueueEmptyException()
        return self._array[self._head]

    def empty(self):
        """
        Checks whether queue is empty.

        :return: True if empty, false otherwise.
        """
        return True if self._len == 0 else False

    def _resize(self, size):
        """
        Resize backing array to specified size.

        :param size: integer value specifying new size.
        """
        new_array = [None] * size

        self._array = new_array


class DynamicArrayQueue(object):
    """
    Custom DynamicArray based Queue implementation.
    """

    def __init__(self):
        """
        Initialize queue.
        """

    def __len__(self):
        """
        Return length of the data structure.

        :return: Number of elements in queue.
        """

    def enqueue(self, element):
        """
        Append element to end of queue.

        :param element: element to append.
        """

    def dequeue(self):
        """
        Remove and return element at front of queue.

        :return: First element in queue.
        """

    def first(self):
        """
        Returns the element at front of queue without removing.

        :return: First element in queue.
        """

    def empty(self):
        """
        Checks whether queue is empty.

        :return: True if empty, false otherwise.
        """


class QueueEmptyException(Exception):
    """
    Denote access to empty stack structure.
    """
    pass
