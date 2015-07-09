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
        Test method for first() and last().
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
        Test before(), after().
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

    def test_add_first(self):
        """
        Test add_first() method.
        """

        # create list and verify add_first...
        l = SingleLinkedList()

        # verify empty list value error
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_first(None)

        l.add_first(node=Node(1))
        l.add_first(Node(2))

        self.assertEqual(2, len(l))
        self.assertEqual(2, l.first().data)
        self.assertEqual(1, l.first().next_node.data)

    def test_add_last(self):
        """
        Test add_last method.
        """

        l = SingleLinkedList()
        self.assertTrue(l.empty())

        n1, n2, n3 = Node(1), Node(2), Node(3)

        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_last(None)

        # add some nodes and verify length, head, tail etc.
        l.add_last(n1)
        self.assertEqual(1, len(l))
        self.assertEqual(l.head, n1)

        l.add_last(n2)
        self.assertEqual(2, len(l))
        self.assertEqual(l.head, n1)
        self.assertEqual(l.tail, n2)

        l.add_last(n3)
        self.assertEqual(3, len(l))
        self.assertEqual(l.head, n1)
        self.assertEqual(l.head.next_node, n2)
        self.assertEqual(l.tail, n3)

        # verify add_last on non-empty list
        n = Node(4)
        l.add_last(n)
        self.assertEqual(n, l.last())

        # verify add_last on empty list
        l = SingleLinkedList()
        n = Node(1)
        l.add_last(n)
        self.assertEqual(n, l.first())
        self.assertEqual(n, l.last())

    def test_add_before(self):
        """
        Test case for add_before method.
        """
        l = SingleLinkedList()
        n0 = Node(0)
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)

        # check "None node" handling
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_before(None, None)
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_before(None, Node(1))
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_before(Node(1), None)
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_before(Node(1), Node(2))

        # verify adding first node.
        l.add_first(n3).add_before(n3, n2).add_first(n1)

        # test existing Node not in list.
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_before(Node(5), Node("Four"))

        # verify list structure.
        l.add_before(n1, n0)
        self.assertEqual(n0, l.first())
        self.assertEqual(n1, l.first().next_node)
        self.assertEqual(n2, l.first().next_node.next_node)
        self.assertEqual(n3, l.first().next_node.next_node.next_node)
        self.assertEqual(None, l.first().next_node.next_node.next_node.next_node)
        self.assertEqual(n3, l.last())

    def test_add_after(self):
        """
        Test case for add_after method.
        """
        l = SingleLinkedList()
        n0 = Node("zero")
        n1 = Node("one")
        n2 = Node("two")
        n3 = Node("three")

        # check "None node" handling
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_after(None, None)
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_after(None, Node(1))
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_after(Node(1), None)
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_after(Node(1), Node(2))

        l.add_first(n3).add_first(n0)

        # add_after a couple of nodes
        l.add_after(n0, n1).add_after(n1, n2)

        self.assertEqual(n0, l.first())
        self.assertEqual(n1, l.first().next_node)
        self.assertEqual(n2, l.first().next_node.next_node)
        self.assertEqual(n3, l.first().next_node.next_node.next_node)
        self.assertEqual(n3, l.last())
        self.assertEqual(None, l.first().next_node.next_node.next_node.next_node)

        # test Node not in list
        # note equal value does not the same node make
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.add_after(Node("three"), Node(4))

    def test_delete_first(self):
        """
        Test delete_first method.
        """
        l = SingleLinkedList()
        # verify empty list value error
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.delete_first()

        # add a couple of nodes
        n1, n2, n3 = Node(1), Node(2), Node(3)
        l.add_last(n1).add_last(n2).add_last(n3)
        self.assertEqual(3, len(l))

        # verify nodes are removed in right order
        self.assertEqual(n1, l.delete_first())
        self.assertEqual(n2, l.delete_first())
        self.assertEqual(n3, l.delete_first())

        self.assertEqual(0, len(l))
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.delete_first()

    def test_delete_last(self):
        """
        Test delete_last method.
        """

        l = SingleLinkedList()
        # verify empty list value error
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.delete_last()

        # add a couple of nodes
        n1, n2, n3 = Node(1), Node(2), Node(3)
        l.add_last(n1).add_last(n2).add_last(n3)
        self.assertEqual(3, len(l))

        # verify nodes are removed in right order
        self.assertEqual(n3, l.delete_last())
        self.assertEqual(n2, l.delete_last())
        self.assertEqual(n1, l.delete_last())

        # self.assertEqual(0, len(l))
        with self.assertRaisesRegex(ValueError, "Not found"):
            l.delete_first()

    def test_delete_before(self):
        """
        TODO: test delete_before method.
        """

    def test_delete_after(self):
        """
        TODO: Test delete_after method.
        """

    def test_delete_at(self):
        """
        TODO: Test delete_at method.
        """

    def test_replace(self):
        """
        TODO: Test replace method.
        """

    def test_repr(self):
        """
        Test __repr__ method.
        """

        l = SingleLinkedList()
        self.assertEquals("[]", l.__repr__())

        l.add_first(Node("Second")).add_first(Node(1))
        self.assertEquals("[Node[1], Node[Second]]", l.__repr__())
        l.add_last(Node("iii"))
        self.assertEquals("[Node[1], Node[Second], Node[iii]]", l.__repr__())
        l.delete_first()
        self.assertEquals("[Node[Second], Node[iii]]", l.__repr__())
        l.delete_last()
        self.assertEquals("[Node[Second]]", l.__repr__())
        l.delete_first()
        self.assertEquals("[]", l.__repr__())
