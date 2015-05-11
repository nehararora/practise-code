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


# TODO: draw_ruler
def draw_english_ruler(scale_length, major_tick_length):
    """
    Draws the markings of a typical English ruler.
    For each inch, places a tick with a numeric label
    :return:
    Section 4.1.2, Data Structures and Algorithms in Python, Goodrich et al.
    """
    pass