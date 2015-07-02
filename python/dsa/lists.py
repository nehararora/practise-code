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
        Return the node preceding the specified node.

        :param node: search Node.
        :return: Node object.
        """

        if self._len <= 1:
            raise ValueError("Not found")

        # prior node needs an actual search in singly linked lists :(
        current = self.head

        while current:
            # went through the list without finding node
            if current.next_node is None:
                raise ValueError("Not found")
            if current.next_node == node:
                # found the node we want.
                return current
            current = current.next_node

    def after(self, node):
        """
        Return the node succeeding specified element.

        :param node: search Node.
        :return: Node object.
        """
        if self._len <= 1 or node.next_node is None:
            raise ValueError("Not found")

        # easy since we have pointer to the next node! :)
        return node.next_node

    def empty(self):
        """
        True if list does not contain elements, false otherwise.

        :return: boolean status.
        """
        return True if self._len == 0 else False

    def append(self, node):
        """
        Append node at end of the list.

        :param node: Node object reference.
        """

        # list is empty.
        if self.head is None:
            self.head = node
        else:
            # make new node current tail's next node.
            self.tail.next_node = node

        # make sure tail now point at new end of list.
        self.tail = node
        self._len += 1

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

    def add_last(self, node):
        """
        Add node at end of list.

        :param node: Node object reference.
        """
        if self.tail is None:
            self.head = node
        else:
            self.tail.next_node = node
        self.tail = node
        self._len += 1

    def add_before(self, node, new_node):
        """
        Add new_node in front of specified node.

        :param node: Node object reference.
        :param new_node: Node object reference.
        """

        if node is None or new_node is None:
            raise ValueError("Not found")

        # need to find the position before node
        current = self.head

        while current:

            # found the position to insert at
            if current.next_node == node:
                # splice new_node between current and node.
                new_node.next_node = current.next_node
                current.next_node = new_node

            # in case we reach the end of the list
            if current.next_node is None:
                raise ValueError("Not found")

            current = current.next_node

    def delete_before(self, node):
        """
        Remove node before specified node.

        :param node: Node object reference.
        """
        # TODO: implement
        return None

    def add_after(self, node):
        """
        Add node after specified node.

        :param node: Node object reference
        """
        # TODO: implement
        return None

    def delete_after(self, node):
        """
        Remove node after specified node.

        :param node: Node object reference
        :return: Removed node.
        """
        # TODO: implement
        return None

    def replace(self, node, replacement):
        """
        Replace specified node with replacement node.

        :param node: Node object reference
        :param replacement: Node object reference
        :return: replaced node.
        """
        # TODO: implement
        return None

    def replace_at(self, position, replacement):
        """
        Replace node at specified position with replacement.

        :param position: Node object reference
        :param replacement: Node object reference
        :return: replaced node.
        """
    def delete_at(self, position):
        """

        :return:
        """
        # TODO: implement
        return None

    def __len__(self):
        """
        Length of list.

        :return: integer count.
        """
        return self._len
