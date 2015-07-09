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

    def __repr__(self):
        """
        Representation.
        """
        return "Node[{}]".format(self.data)


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
                raise ValueError("{} Not found".format(node))
            if current.next_node == node:
                # found the node we want.
                return current
            current = current.next_node

        # node not found in list.
        raise ValueError("Not found")

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

    def add_first(self, node):
        """
        Add Node at head of list.

        :param node: Node object reference.
        :return: List reference.
        """

        if node is None:
            raise ValueError("Not found")

        # insert at front of list
        if self.head is not None:
            node.next_node = self.head
        else:
            # handle first node case
            self.tail = node

        self.head = node
        self._len += 1
        return self

    def add_last(self, node):
        """
        Append node at end of the list.

        :param node: Node object reference.
        :return: List reference.
        """

        if node is None:
            raise ValueError("Not found")

        # list is empty.
        if self.head is None:
            self.head = node
        else:
            # make new node current tail's next node.
            self.tail.next_node = node

        # make sure tail now points at new end of list.
        self.tail = node
        self._len += 1
        return self

    def add_before(self, node, new_node):
        """
        Add new_node in front of specified node.

        :param node: Node object reference.
        :param new_node: Node object reference.
        """

        if node is None or new_node is None or self.head is None:
            raise ValueError("Not found")

        # Handle the first node - before() not defined for lists of size 1.
        if self.head == node:
            # if this was the head node, make new_node the head.
            new_node.next_node = self.head
            self.head = new_node

            self._len += 1
            return self

        # find the  node to insert after
        prev = self.before(node)
        new_node.next_node = prev.next_node
        prev.next_node = new_node
        self._len += 1
        return self

    def add_after(self, node, new_node):
        """
        Add node after specified node.
        adding a node is straightforward, but still need to check
        if node is in the list.

        :param node: Node object reference.
        :param new_node: Replacement node object reference.
        """
        # null checks
        if node is None or new_node is None or self.head is None:
            raise ValueError("Not found")

        current = self.head
        while current:
            # make sure node is in list
            if current == node:
                break
            current = current.next_node

        # node is not actually in the list
        if current is None:
            raise ValueError("Not found")

        # splice new_node after node - if node points to None so be it.
        new_node.next_node = node.next_node
        node.next_node = new_node
        # adjust tail if needed
        self.tail = new_node if self.tail is node else self.tail
        self._len += 1

        return self

    def delete_first(self):
        """
        Remove node from head of the list.

        :return: removed Node object.
        """
        if self.head is None:
            raise ValueError("Not found")

        # grab the first node from list
        n = self.head
        # move the head "pointer" to next node.
        self.head = self.head.next_node

        # if there is no next node, make tail None as well
        if self.head is None:
            self.tail = self.head
        self._len -= 1
        return n

    def delete_last(self):
        """
        Remove node from tail of the list.

        In a singly linked list this is o(n) - need to traverse
        to find the prior-to-last node.

        :return: removed Node object reference.
        """
        if self._len == 0:
            raise ValueError("Not found")

        # only node in the list
        if self.head == self.tail:
            n = self.head
            self.head = self.tail = None
            self._len = 0
            return n

        # if more than one node, find the last.
        current = self.head
        while current.next_node:
            # found the prior to last node
            if current.next_node is self.tail:
                break
            current = current.next_node

        # remove the last node and move tail
        n = current.next_node
        self.tail = current
        current.next_node = None
        self._len += 1
        return n

    def delete_before(self, node):
        """
        Remove node before specified node.

        :param node: Node object reference.
        """
        # TODO: delete_before
        return None

    def delete_after(self, node):
        """
        Remove node after specified node.

        :param node: Node object reference
        :return: Removed node.
        """
        # TODO: delete_after
        return None

    def empty(self):
        """
        True if list does not contain elements, false otherwise.

        :return: boolean status.
        """
        return True if self._len == 0 else False

    def replace(self, node, replacement):
        """
        Replace specified node with replacement node.

        :param node: Node object reference
        :param replacement: Node object reference
        :return: replaced node.
        """
        # TODO: replace
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
        # TODO: delete_at
        return None

    def __len__(self):
        """
        Length of list.

        :return: integer count.
        """
        return self._len

    def __repr__(self):
        """
        Representation.
        """
        l = []
        current = self.head
        while current:
            l.append(str(current))
            current = current.next_node

        return "[{}]".format(", ".join(l))
