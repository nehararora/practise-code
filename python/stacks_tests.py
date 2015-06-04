"""
stacks_tests.py: Test cases for Stack implementations.

"""

__author__ = 'nehar'


import unittest

from stacks import ArrayStack
from stacks import DynamicArrayStack
from stacks import StackEmptyException


class TestArrayStack(unittest.TestCase):

    def test_instantiation(self):
        """
        Test basic object creation.
        """
        s = ArrayStack()
        self.assertEqual(0, len(s))
        self.assertEqual(0, len(s._array))

    def test_push(self):
        """
        Test stack push operation.
        """

        s = ArrayStack()
        self.assertEqual(0, len(s))

        # basic push
        s.push(1)
        self.assertEqual(1, len(s))
        self.assertEqual(1, len(s._array))
        self.assertEqual(1, s._array[0])

        # push an object
        s.push(StackEmptyException)
        self.assertEqual(2, len(s))
        self.assertEqual(2, len(s._array))
        self.assertEqual(StackEmptyException, s._array[1])

    def test_pop(self):
        """
        Test stack pop operation.
        """

        s = ArrayStack()
        s.push(1)
        s.push(2)
        s.push(StackEmptyException)
        self.assertEqual(3, len(s))
        self.assertEqual(StackEmptyException, s.pop())
        self.assertEqual(2, len(s))
        self.assertEqual(2, s.pop())
        self.assertEqual(1, len(s))
        self.assertEqual(1, s.pop())
        self.assertEqual(0, len(s))
        with self.assertRaises(StackEmptyException):
            s.pop()

    def test_peek(self):
        """
        Test stack peek.
        """
        s = ArrayStack()
        self.assertEqual(0, len(s))

        with self.assertRaises(StackEmptyException):
            s.peek()

        # try a basic peek
        s.push(1)
        self.assertEqual(1, s.peek())

        # try peeking with simple object
        s.push([1, 2])
        self.assertEqual([1, 2], s.peek())


class TestDynamicArrayStack(unittest.TestCase):

    def test_instantiation(self):
        """
        Test basic object creation.
        """
        s = DynamicArrayStack()
        self.assertEqual(0, len(s))
        self.assertEqual(0, len(s._array))

    def test_push(self):
        """
        Test stack push operation.
        """

        s = DynamicArrayStack()
        self.assertEqual(0, len(s))

        # basic push
        s.push(1)
        self.assertEqual(1, len(s))
        self.assertEqual(1, len(s._array))
        self.assertEqual(1, s._array[0])

        # push an object
        s.push(StackEmptyException)
        self.assertEqual(2, len(s))
        self.assertEqual(2, len(s._array))
        self.assertEqual(StackEmptyException, s._array[1])

    def test_pop(self):
        """
        Test stack pop operation.
        """

        s = DynamicArrayStack()
        s.push(1)
        s.push(2)
        s.push(StackEmptyException)
        self.assertEqual(3, len(s))
        self.assertEqual(StackEmptyException, s.pop())
        self.assertEqual(2, len(s))
        self.assertEqual(2, s.pop())
        self.assertEqual(1, len(s))
        self.assertEqual(1, s.pop())
        self.assertEqual(0, len(s))
        with self.assertRaises(StackEmptyException):
            s.pop()

    def test_peek(self):
        """
        Test stack peek.
        """
        s = DynamicArrayStack()
        self.assertEqual(0, len(s))

        with self.assertRaises(StackEmptyException):
            s.peek()

        # try a basic peek
        s.push(1)
        self.assertEqual(1, s.peek())

        # try peeking with simple object
        s.push([1, 2])
        self.assertEqual([1, 2], s.peek())
