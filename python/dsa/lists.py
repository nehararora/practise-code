"""
lists.py: Basic linked list data structure implementations.

refer: Chapter 7, Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'


class Node(object):
    __slots__ = "data", "next_node"

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __eq__(self, other):
        """
        Returns True if both object references are same.

        :param other: Node object.
        :return: boolean status
        """
        return self is other

    def __ne__(self, other):
        """
        Returns True if object references are not the same.

        :param other: Node object to compare.
        :return: boolean status
        """
        return not self.__eq__(other)


class SingleLinkedList(object):
    """
    Singly linked list data structure.
    """

    def __init__(self, head=None):
        """
        Initialize list with head node (if passed in.)

        :param head: head node of list.
        """
        self._len = 0 if head is None else 1
        self.head = head
        self.tail = head

    def first(self):
        """
        Return the head node.

        :return: Node object.
        """
        return None if self.head is None else self.head

    def last(self):
        """
        Return the tail element.

        :return: Node object.
        """
        return None if self.tail is None else self.tail

    def before(self, node):
        """
        Return the node preceding the specified data.

        :param node: search element.
        :return: Node object.
        """
        # TODO: implement

    def after(self, node):
        """
        Return the node succeeding the first occurrence of data.

        :param node: search element.
        :return: Node object.
        """
        # TODO: implement

    def empty(self):
        """
        True if list does not contain elements, false otherwise.

        :return: boolean status.
        """
        return True if self._len == 0 else False

    def add_first(self, node):
        """
        Add Node at head of list.

        :param node: Node object reference.
        """

        # insert at front of list
        if self.head is not None:
            node.next_node = self.head
        else:
            # handle first node case
            self.tail = node

        self.head = node
        self._len += 1

    def add_last(self):
        """

        :return:
        """
        # TODO: implement

    def add_before(self):
        """

        :return:
        """
        # TODO: implement

    def delete_before(self):
        """

        :return:
        """
        # TODO: implement

    def add_after(self):
        """

        :return:
        """
        # TODO: implement

    def delete_after(self):
        """

        :return:
        """
        # TODO: implement

    def replace(self):
        """

        :return:
        """
        # TODO: implement

    def delete_at(self):
        """

        :return:
        """
        # TODO: implement

    def __len__(self):
        """
        Length of list.

        :return: integer count.
        """
        return self._len
