"""
stacks.py: Stack based implementations.

refer: Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'

from arrays import DynamicArray


class ArrayStack(object):
    """
    List (array) based stack implementation.
    """

    def __init__(self, max_len=None):
        """
        Initialize stack.
        """
        self._array = []
        self._max = max_len

    def __len__(self):
        """
        Returns the size of the stack.

        :return: Number of elements in stack.
        """
        return len(self._array)

    def __str__(self):
        """
        String representation of stack object.

        :return: String representation.
        """
        return str(self._array)

    def push(self, item):
        """
        Push an element onto the top of the stack.

        :param item: Element to place at top of stack.
        """
        # if max size is defined check stack size.
        if self._max is not None and len(self) == self._max:
            raise StackFullException

        self._array.append(item)

    def pop(self):
        """
        Remove and return the topmost element on stack.

        :return: Last inserted element.
        """
        if len(self._array) == 0:
            raise StackEmptyException
        return self._array.pop()

    def peek(self):
        """
        Examine (return) the top element without removing from stack.

        :return: Last inserted element.
        """
        if self.empty():
            raise StackEmptyException()

        return self._array[-1]

    def empty(self):
        """
        Checks whether stack is empty.

        :return: True if empty, false otherwise.
        """
        return True if len(self._array) == 0 else False

    def transfer(self, to):
        """
        Transfer all elements from calling object onto the input stack so that
        the element that starts at the top of calling stack is the first to be
        inserted onto the "to" stack, and the element at the bottom of calling
        stack ends up at the top of "to" stack.

        Exercises C-6.3, Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.

        :param to: Stack to transfer elements to.
        """

        for i in range(len(self)):
            to.push(self.pop())

    def remove_all(self):
        """
        Recursive method for removing all the elements from a stack.

        Exercises C-6.4, Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.
        """
        if len(self) == 0:
            return
        self.pop()
        self.remove_all()

    def reverse(self, lst):
        """
        Reverse a list of elements by pushing them onto the stack, and writing
        them back to the list in reverse order.

        Exercises C-6.5, Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.

        :param lst: original list
        :return: list in reverse order from original.
        """
        for l in lst:
            self.push(l)
        rev_list = []
        for i in range(len(lst)):
            rev_list.append(self.pop())
        return rev_list

class DynamicArrayStack(object):
    """
    Custom DynamicArray based stack implementation.
    """

    def __init__(self):
        """
        Initialize stack.
        """
        self._array = DynamicArray()

    def __len__(self):
        """
        Returns the size of the stack.

        :return: Number of elements in stack.
        """
        return len(self._array)

    def push(self, item):
        """
        Push an element onto the top of the stack.

        :param item: Element to place at top of stack.
        """
        self._array.append(item)

    def pop(self):
        """
        Remove and return the topmost element on stack.

        :return: Last inserted element.
        """
        if len(self._array) == 0:
            raise StackEmptyException
        return self._array.pop()

    def peek(self):
        """
        Examine (return) the top element without removing from stack.

        :return: Last inserted element.
        """
        if self.empty():
            raise StackEmptyException()

        return self._array[-1]

    def empty(self):
        """
        Checks whether stack is empty.

        :return: True if empty, false otherwise.
        """
        return True if len(self._array) == 0 else False

class StackEmptyException(Exception):
    """
    Denote access to empty stack structure.
    """
    pass


class StackFullException(Exception):
    """
    Denote access to a full stack structure.
    """
    pass


def paren_matcher(expression):
    """
    Parentheses matcher, returns true if  expression contains balanced parenthetical symbols - (,{,[, ], }, )
    i.e. all opening symbols have corresponding closing symbols in the correct order.

    Section 6.1.4, Chapter 6, Data Structures and Algorithms in Python, Goodrich et al.
    :param expression: expression containing parenthetical symbols.
    :return: True if expression is balanced, False otherwise.
    """

    # stack to track opening and closing brackets
    s = DynamicArrayStack()
    matches = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    for symbol in expression:
        # push opening parens onto stack
        if symbol in matches.keys():
            s.push(symbol)
        # if next is closing symbol, need to look for match on top of stack.
        elif symbol in matches.values():
            # if stack is already empty we've found an unbalanced closer.
            if s.empty():
                return False
            # if "opener" on top of stack doesn't match the "closer", unbalanced.
            if symbol != matches[s.pop()]:
                return False

    # if stack is now empty we're balanced!
    return s.empty()

