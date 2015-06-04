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

        # push an object
        s.enqueue(QueueEmptyException)
        self.assertEqual(2, len(s))
        self.assertEqual(5, len(s._array))
        self.assertEqual(QueueEmptyException, s._array[1])
        self.assertEqual(1, s.first())
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


class TestDynamicArrayStack(unittest.TestCase):

    def test_instantiation(self):
        """
        Test basic object creation.
        """
        s = DynamicArrayQueue()
        self.assertEqual(0, len(s))
        self.assertEqual(0, len(s._array))

    def test_push(self):
        """
        Test stack push operation.
        """

        s = DynamicArrayQueue()
        self.assertEqual(0, len(s))

        # basic push
        s.push(1)
        self.assertEqual(1, len(s))
        self.assertEqual(1, len(s._array))
        self.assertEqual(1, s._array[0])

        # push an object
        s.push(QueueEmptyException)
        self.assertEqual(2, len(s))
        self.assertEqual(2, len(s._array))
        self.assertEqual(QueueEmptyException, s._array[1])

    def test_pop(self):
        """
        Test stack pop operation.
        """

        s = DynamicArrayQueue()
        s.push(1)
        s.push(2)
        s.push(QueueEmptyException)
        self.assertEqual(3, len(s))
        self.assertEqual(QueueEmptyException, s.pop())
        self.assertEqual(2, len(s))
        self.assertEqual(2, s.pop())
        self.assertEqual(1, len(s))
        self.assertEqual(1, s.pop())
        self.assertEqual(0, len(s))
        with self.assertRaises(QueueEmptyException):
            s.pop()

    def test_peek(self):
        """
        Test stack peek.
        """
        s = DynamicArrayQueue()
        self.assertEqual(0, len(s))

        with self.assertRaises(QueueEmptyException):
            s.peek()

        # try a basic peek
        s.push(1)
        self.assertEqual(1, s.peek())

        # try peeking with simple object
        s.push([1, 2])
        self.assertEqual([1, 2], s.peek())



