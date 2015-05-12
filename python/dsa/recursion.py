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
class Ruler(object):

    def __init__(self, inches, major_length, tick_label=''):
        self.inches = inches
        self.major_length = major_length
        self.tick_label = tick_label

    def draw(self):
        """
        Draws the markings of a typical English ruler.
        For each inch, places a tick with a numeric label
        :return:
        Section 4.1.2, Data Structures and Algorithms in Python, Goodrich et al.
        """
        self.draw_line(self.major_length, '0')  # draw line 0
        for j in range(1, 1 + self.inches):
            self.draw_interval(self.major_length - 1)
            self.draw_line(self.major_length, str(j))  # draw lin j

    @staticmethod
    def draw_line(tick_length, tick_label=''):
        line = '-' * tick_length
        if tick_label:
            line += ' ' + tick_label
        print(line)

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