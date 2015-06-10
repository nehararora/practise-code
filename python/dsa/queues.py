"""
queues.py: Queue data structure implementations.

refer: Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'

import collections

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
            self._resize(2 * len(self._array))

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

        # shrink array by half if less that 1/4 full
        if 0 < self._len < len(self._array)//4:
            self._resize(len(self._array)//2)

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

        # move elements starting with the front (which may not be at 0'th index)
        i = self._head

        # move all existing elements over
        for j in range(self._len):
            new_array[j] = self._array[i]
            # reposition pointer in circular list
            i = (i + 1) % len(self._array)

        self._array = new_array
        self._head = 0


class DequeQueue(object):
    """
    collections.deque based queue.

    Simple adapter that implements the queue ADT using
    a collections.deque instance for storage.

    Exercises R-6.11, Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.
    """

    def __init__(self, max_len=5):
        """
        Initialize queue.
        """
        self._array = collections.deque(maxlen=max_len)
        self._len = 0

    def __len__(self):
        """
        Return length of the data structure.

        :return: Number of elements in queue.
        """
        return self._len

    def enqueue(self, element):
        """
        Append element to start (left end) of queue.

        will resize on overflow.

        :param element: element to append.
        """
        # resize on overflow
        if self._array.maxlen == self._len:
            self._resize(2 * len(self._array))

        # enqueue and increment count
        self._array.appendleft(element)
        self._len += 1

    def dequeue(self):
        """
        Remove and return element at end of queue.

        :return: First element in queue.
        """
        if self.empty():
            raise QueueEmptyException()
        data = self._array.pop()
        self._len -= 1

        # shrink array by half if less that 1/4 full
        if 0 < self._len < len(self._array)//4:
            self._resize(len(self._array)//2)

        return data

    def first(self):
        """
        Returns the element at front of queue without removing.

        :return: First element in queue.
        """
        if self.empty():
            raise QueueEmptyException()

        # simulate first using pop and push
        data = self._array.pop()

        self._array.append(data)
        return data

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
        new_array = collections.deque(maxlen=size)

        # move all existing elements over
        for element in self._array:
            new_array.append(element)

        self._len = len(self._array)
        self._array = new_array

class QueueEmptyException(Exception):
    """
    Denote access to empty stack structure.
    """
    pass

# TODO: implement
class ArrayDeque(object):
    """
    Array/List based deque.
    """

    def add_first(self, element):
        """
        Add element to the front of the deque.

        :param element: Object to be added.
        """

    def add_last(self, element):
        """
        add element to end of the deque.

        :param element: Object to be added.
        """

    def delete_first(self):
        """
        Remove the first element from the deque.

        :return: Removed object.
        """

    def delete_last(self):
        """
        Remove the last element from deque.

        :return: Removed object.
        """

    def first(self):
        """
        Returns the element at front of queue without removing.

        :return: Element at front of the deque.
        """

    def last(self):
        """
        Returns the element at the end of the queue without removing.

        :return: Element at end of the deque.
        """

    def empty(self):
        """
        Check whether deque is empty.

        :return: True if empty, false otherwise.
        """

    def __len__(self):
        """
        Return length of the deque.

        :return: Number of elements in queue.
        """
