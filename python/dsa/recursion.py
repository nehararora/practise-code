"""
recursion.py: Recursion based algorithms.

primarily Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.

"""
__author__ = 'nehar'


def factorial(n):
    """
    Basic recursive factorial.
    O(n)
    """

    if type(n) is not int or n < 0:
        raise ValueError

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def binary_search(data, target, low, high):
    """
    Recursive binary search implementation.

    :param data:
    :param target:
    :param low:
    :param high:
    :return:
    """

    if low > high:
        return False
    else:
        # find the mid point
        mid = (low + high)//2

        if data[mid] == target:
            return True

        elif data[mid] > target:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)


def recursive_sum(seq=[]):
    """
    Recursive sum of elements of a sequence.
    O(n) since n recursions, each constant time.
    Section 4.3.1, Data Structures and Algorithms in Python, Goodrich et al.

    :param seq: Sequence of elements
    :return: Sum
    """
    n = len(seq)
    if n == 0:
        return 0
    else:
        return recursive_sum(seq[0:n-1]) + seq[n-1]


def recursive_reverse(seq=[]):
    """
    Reverses elements of sequence using linear recursion.
    O(n) since each activation remove 2 elements.
    Section 4.4, Data Structures and Algorithms in Python, Goodrich et al.

    :param seq: Sequence to be reversed
    :return: Reversed sequence
    """

    n = len(seq)
    # consider a 0 length sequence reversed as well
    if n == 0 or n == 1:
        return seq

    # swap the elements at the end and recurse
    return [seq[n-1]] + recursive_reverse(seq[1:n-1]) + [seq[0]]


def naive_power(x, n):
    """
    Raises x to the power n (x^n) using recursion.

    :param x:
    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return x * naive_power(x, n-1)

class Ruler(object):
    """
    Recursive implementation of a typical English ruler.

    Section 4.1.2, Data Structures and Algorithms in Python, Goodrich et al.
    """
    def __init__(self, inches, major_length, tick_label=''):
        self.inches = inches
        self.major_length = major_length
        self.tick_label = tick_label
        self.ruler = ''

    def draw(self):
        """
        Draw - For each inch, places a tick with a numeric label
        :return:
        Section 4.1.2, Data Structures and Algorithms in Python, Goodrich et al.
        """
        self.draw_line(self.major_length, '0')  # draw line 0
        for j in range(1, 1 + self.inches):
            self.draw_interval(self.major_length - 1)
            self.draw_line(self.major_length, str(j))  # draw lin j
        return self.ruler

    def draw_line(self, tick_length, tick_label=''):
        line = '-' * tick_length
        if tick_label:
            line += ' ' + tick_label

        # add current line to the ruler
        self.ruler += line + '\n'

    def draw_interval(self, center_length):
        """
        Draws the interval.
        :param center_length: Length of the central tick line for this interval.
        :return:
        """

        # Draw, top edge, center ticks, and bottom edge
        if center_length > 0:
            self.draw_interval(center_length - 1)
            self.draw_line(center_length)
            self.draw_interval(center_length - 1)