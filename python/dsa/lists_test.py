"""
lists_test.py:Linked list test module.

"""

__author__ = 'nehar'

import unittest
from lists import SingleLinkedList
from lists import Node


class TestSingleLinkedList(unittest.TestCase):
    """
    Single linked list test class.
    """

    def test_instantiation(self):
        """
        Basic object creation test.
        """
        l = SingleLinkedList()
        self.assertEqual(None, l.head)
        self.assertEqual(0, l._len)
        self.assertTrue(l.empty())

        n = Node()
        self.assertEqual(None, n.data)
        self.assertEqual(None, n.next_node)

        n = Node(1)
        self.assertEqual(1, n.data)
        self.assertEqual(None, n.next_node)

        m = Node(data=2, next_node=n)
        self.assertEqual(2, m.data)
        self.assertEqual(n, m.next_node)

    def test_equality(self):
        """
        Test equality operations.
        """
        n1, n2 = Node(1), Node(2)

        self.assertEqual(n1, n1)
        self.assertNotEqual(n1, n2)

    def test_first_last(self):
        """
        """
        l = SingleLinkedList()
        self.assertIsNone(l.first())
        self.assertIsNone(l.last())

        n = Node("foo")
        l.add_first(n)
        self.assertEqual(n, l.first())
        self.assertEqual("foo", l.first().data)
        self.assertEqual(n, l.last())
        self.assertEqual("foo", l.last().data)

        m = Node("bar")
        l.add_first(m)
        self.assertEqual(m, l.first())
        self.assertEqual("bar", l.first().data)
        self.assertEqual(n, l.last())
        self.assertEqual("foo", l.last().data)

    def test_before_after(self):
        """
        Test before(), after()
        """
        l = SingleLinkedList()
        with self.assertRaises(ValueError):
            l.before(None)

        n = Node("Hello")
        l.add_first(n)
        with self.assertRaises(ValueError):
            l.before(n)

        l = SingleLinkedList()
        n1, n2 = Node("Foo"), Node("Bar")
        l.add_first(n1)
        l.add_last(n2)
        print(l.head.data, l.tail.data)
        self.assertEqual(n1, l.before(n2))

        with self.assertRaises(ValueError):
            l.before(Node("Not in list"))

        # test after()
        l = SingleLinkedList()
        with self.assertRaises(ValueError):
            l.after(Node(1))

        n1, n2 = Node("Foo"), Node("Bar")
        l.add_first(n1)
        with self.assertRaises(ValueError):
            l.after(n1)

        l.add_last(n2)
        self.assertEqual(n2, l.after(n1))

    def test_empty(self):
        """
        Test empty status.
        """
        l = SingleLinkedList()
        self.assertTrue(l.empty())

        l.add_first(2)
        self.assertFalse(l.empty())
        self.assertEqual(1, len(l))
        self.assertEqual(1, l._len)

    def test_add_first_last(self):
        """
        Test add_first() and add_last()
        """

        # create list and verify add_first...
        l = SingleLinkedList()

        l.add_first(node=Node(1))
        l.add_first(Node(2))

        self.assertEqual(2, len(l))
        self.assertEqual(2, l.first().data)
        self.assertEqual(1, l.last().data)

        # verify add_last on non-empty list
        n = Node(3)
        l.add_last(n)
        self.assertEqual(n, l.last())

        # verify add_last on empty list
        l = SingleLinkedList()
        n = Node(1)
        l.add_last(n)
        self.assertEqual(n, l.first())
        self.assertEqual(n, l.last())

    def test_add_before_after(self):
        """

        :return:
        """
    def test_delete_before_after(self):
        """

        :return:
        """

    def test_delete_at(self):
        """

        :return:
        """

    def test_replace(self):
        """

        :return:
        """