"""
queues_tests.py: Test cases for Queue implementations.

"""

__author__ = 'nehar'


import unittest

from queues import ArrayQueue
from queues import DynamicArrayQueue
from queues import QueueEmptyException

class TestArrayQueue(unittest.TestCase):

    def test_instantiation(self):
        """
        Test basic object creation.
        """
        s = ArrayQueue()
        self.assertEqual(0, len(s))

        # backing array defaults to static capacity...
        self.assertEqual(5, len(s._array))

        # change class internal and try again...
        ArrayQueue.ARRAY_SIZE = 10
        s = ArrayQueue()
        self.assertEqual(0, len(s))
        self.assertEqual(10, len(s._array))
        # change back to original
        ArrayQueue.ARRAY_SIZE = 5

    def test_enqueue(self):
        """
        Test stack push operation.
        """

        s = ArrayQueue()
        self.assertEqual(0, len(s))

        # basic push
        s.enqueue(1)
        self.assertEqual(1, len(s))
        self.assertEqual(5, len(s._array))
        self.assertEqual(1, s.first())
        self.assertEqual(1, s._array[0])

        # add another object
        s.enqueue(QueueEmptyException)
        self.assertEqual(2, len(s))
        self.assertEqual(5, len(s._array))
        self.assertEqual(QueueEmptyException, s._array[1])
        self.assertEqual(1, s.first())

        # remove front and check new first
        self.assertEqual(1, s.dequeue())
        self.assertEqual(QueueEmptyException, s.first())

    def test_dequeue(self):
        """
        Test Queue dequeue operation.
        """

        s = ArrayQueue()
        s.enqueue(1)
        s.enqueue(2)
        s.enqueue(QueueEmptyException)
        self.assertEqual(3, len(s))
        self.assertEqual(1, s.dequeue())
        self.assertEqual(2, len(s))
        self.assertEqual(2, s.dequeue())
        self.assertEqual(1, len(s))
        self.assertEqual(QueueEmptyException, s.dequeue())
        self.assertEqual(0, len(s))
        with self.assertRaises(QueueEmptyException):
            s.dequeue()

    def test_resize(self):
        """
        Test backing array resize.
        """
        s = ArrayQueue()
        self.assertEqual(5, len(s._array))

        # check capacity increase
        s.enqueue(1)
        s.enqueue(2)
        s.enqueue(3)
        s.enqueue(4)
        s.enqueue(5)
        self.assertEqual(5, len(s))
        self.assertEqual(5, s._len)
        self.assertEqual(5, len(s._array))

        s.enqueue(6)
        self.assertEqual(6, len(s))
        self.assertEqual(6, s._len)
        self.assertEqual(10, len(s._array))

        # verify shrinking array size
        self.assertEqual(1, s.dequeue())
        self.assertEqual(2, s.dequeue())
        self.assertEqual(3, s.dequeue())
        self.assertEqual(4, s.dequeue())

        self.assertEqual(2, len(s))
        self.assertEqual(10, len(s._array))

        self.assertEqual(5, s.dequeue())

        self.assertEqual(1, len(s))
        self.assertEqual(5, len(s._array))

    def test_first(self):
        """
        Test Queue first.
        """
        s = ArrayQueue()
        self.assertEqual(0, len(s))

        with self.assertRaises(QueueEmptyException):
            s.first()

        # first() always returns object at front of queue...
        s.enqueue(1)
        self.assertEqual(1, s.first())
        s.enqueue([1, 2])
        self.assertEqual(1, s.first())
        self.assertEqual(1, s.dequeue())
        self.assertEqual([1, 2], s.first())
        self.assertEqual([1, 2], s.dequeue())
        with self.assertRaises(QueueEmptyException):
            s.first()
