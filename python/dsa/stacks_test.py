"""
stacks_tests.py: Test cases for Stack implementations.

"""

__author__ = 'nehar'


import unittest

from stacks import ArrayStack
from stacks import DynamicArrayStack
from stacks import StackEmptyException
from stacks import StackFullException
from stacks import paren_matcher


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

    def test_transfer(self):
        """
        Test stack transfer
        """
        s1 = ArrayStack()
        s2 = ArrayStack()

        # add a few elements
        s1.push(1)
        s1.push(2)
        s1.push(3)
        self.assertEqual("[1, 2, 3]", str(s1))
        self.assertEqual("[]", str(s2))

        # transfer into s2 and verify
        s1.transfer(s2)
        self.assertEqual("[3, 2, 1]", str(s2))
        self.assertEqual("[]", str(s1))

    def test_remove_all(self):
        """
        Test recursive remove all.
        """
        s = ArrayStack()
        s.push(1)
        s.push(1)
        s.push(1)
        self.assertEqual(3, len(s))
        s.remove_all()
        self.assertEqual(0, len(s))

        s = ArrayStack()
        self.assertEqual(0, len(s))
        s.remove_all()
        self.assertEqual(0, len(s))

    def test_reverse(self):
        """
        Test reverse list.
        """
        s = ArrayStack()
        lst = [1, 2, 3, 4]
        self.assertEqual([4, 3, 2, 1], s.reverse(lst))

        self.assertEqual([], s.reverse([]))
        self.assertEqual(['a'], s.reverse(['a']))

    def test_max_length(self):
        """
        Test maximum stack size limit.
        """
        s = ArrayStack(max_len=4)
        s.push(1)
        s.push(1)
        s.push(1)
        s.push(1)
        with self.assertRaises(StackFullException):
            s.push(1)


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


class TestParenChecker(unittest.TestCase):
    """
    Test cases for stack based parentheses checker.
    """
    def test_paren(self):

        self.assertEqual(False, paren_matcher("[{["))
        self.assertEqual(False, paren_matcher(")(()){([()])}"))
        self.assertEqual(False, paren_matcher("({[])}"))
        self.assertEqual(False, paren_matcher("("))

        # our implementation considers no parens as balanced
        self.assertEqual(True, paren_matcher(""))
        # same for other expressions.
        self.assertEqual(True, paren_matcher("123"))

        self.assertEqual(True, paren_matcher("[]"))
        self.assertEqual(True, paren_matcher("()"))
        self.assertEqual(True, paren_matcher("{}"))
        self.assertEqual(True, paren_matcher("[[[[ {[ ({[ ]}) ]} ]]]]"))
        self.assertEqual(True, paren_matcher("()(()){([()])}"))
        self.assertEqual(True, paren_matcher("((()(()){([()])}))"))
