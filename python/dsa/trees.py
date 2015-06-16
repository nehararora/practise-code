"""
trees.py: Basic Tree data structure algorithm implementations.

refer: Chapter 8, Data Structures and Algorithms in Python, Goodrich et al.
"""

__author__ = 'nehar'

from abc import ABCMeta, abstractmethod


class TreeADT(metaclass=ABCMeta):
    """
    The Tree abstract data type.
    """
    @abstractmethod
    def root(self):
        """
        Return root node of Tree.

        :return: Node
        """
        pass

    @abstractmethod
    def is_root(self, node):
        """
        Returns True if node is root of Tree.

        :param node: Node object to check.
        :return: boolean
        """
        pass

    @abstractmethod
    def parent(self, node):
        """
        Return parent of input node.

        :param node: child Node object
        :return: parent Node object
        """
        pass

    @abstractmethod
    def children(self, node):
        """
        Generate an iteration of node's children.

        :param node: parent Node object
        :return: Children Node objects.
        """

    @abstractmethod
    def is_leaf(self, node):
        """
        Return True if node is a leaf node (i.e. no children), false otherwise.

        :param node: Node object.
        :return: boolean
        """

    @abstractmethod
    def __len__(self):
        """
        Return count of nodes in tree.

        :return: Integer count
        """

    @abstractmethod
    def empty(self):
        """
        Return True if tree is empty (i.e. no nodes), false otherwise.

        :return: boolean
        """

    @abstractmethod
    def __iter__(self):
        """
        Iterator for tree.
        :return: iter
        """

