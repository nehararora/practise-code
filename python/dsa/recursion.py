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


def sum_linear(seq=None):
    """
    Linear recursive sum of elements of a sequence.
    O(n) since n recursions, each constant time.
    Section 4.3.1, Data Structures and Algorithms in Python, Goodrich et al.

    :param seq: Sequence of elements
    :return: Sum
    """
    if not seq:
        seq = []
    n = len(seq)
    if n == 0:
        return 0
    else:
        return sum_linear(seq[0:n-1]) + seq[n-1]


def sum_binary(seq=None):
    """
    Binary recursive sum of elements of a sequence.
    O(n) running time since 2n-1 fx calls
    Section 4.4, Data Structures and Algorithms in Python, Goodrich et al.
    :param seq:
    :return:
    """
    if not seq:
        seq = []
    n = len(seq)
    if n == 0:
        return 0
    elif n == 1:
        return seq[0]
    else:
        mid = n//2
        return sum_binary(seq[0:mid]) + sum_binary(seq[mid:n])


def find_max(seq=None):
    """
    A recursive algorithm for finding the maximum element in a sequence, S, of n elements.

    Exercise R-4.1, Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.
    :param seq:
    :return:
    """
    if not seq:
        seq = []
    n = len(seq)
    # only element in list is max by itself
    if n == 0:
        raise TypeError
    elif n == 1:
        return seq[0]

    x = find_max(seq[0:n-1])

    return seq[n-1] if seq[n-1] > x else x


def find_min_max(seq=None):
    """
    Function to find minimum and maximum values in a sequence (without using loops.)
    Exercise C-4.9, Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.
    :param seq: Input sequence
    :return: a tuple of minimum and maximum values from seq.
    """
    if not seq:
        seq = []

    n = len(seq)
    if n == 0:
        raise TypeError
    if n == 1:
        return seq[0], seq[0]
    if n == 2:
        return (seq[0], seq[1]) if seq[0] < seq[1] else (seq[1], seq[0])

    min_val, max_val = find_min_max(seq[0:n-2])

    min_val = seq[n-1] if seq[n-1] < min_val else min_val
    min_val = seq[n-2] if seq[n-2] < min_val else min_val
    max_val = seq[n-1] if seq[n-1] > max_val else max_val
    max_val = seq[n-2] if seq[n-2] > max_val else max_val

    return min_val, max_val


def product(m, n):
    """
    Recursive algorithm to compute the product of two positive integers,
    m and n, using only addition and subtraction.

    Exercise C-4.12, Chapter 4, Data Structures and Algorithms in Python,
    Goodrich et al.
    """
    if type(m) is not int:
        raise TypeError
    if type(n) is not int:
        raise TypeError

    if m < 0 or n < 0:
        raise TypeError

    if m == 0 or n == 0:
        return 0
    if n == 1:
        return m

    return m + product(m, n-1)


def recursive_reverse(seq=None):
    """
    Reverses elements of sequence using linear recursion.
    O(n) since each activation remove 2 elements.
    Section 4.4, Data Structures and Algorithms in Python, Goodrich et al.

    :param seq: Sequence to be reversed
    :return: Reversed sequence
    """
    if not seq:
        seq = []

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


def recurrence_power(x, n):
    """
    Raises x to the power n using the recurrence relation.
    power(x, n)
        = 1 if n==0
        = x * power(x, ceil(n/2))^2 if n > 0 is odd
        = (power(x, ceil()n/2))^2   if n > 0 is even

    running time ~ O(log(n)) as n is halved each time.
    :param x: base
    :param n: exponent
    :return: x**n
    """
    if n == 0:
        return 1
    else:
        # create partial
        partial = recurrence_power(x, n//2)
        # square to get results
        result = partial * partial

        # if odd, include the extra x
        if n % 2 == 1:
            result *= x
        return result


def harmonic_number(n):
    """
    Describe a recursive function for computing the nth Harmonic number, Hn = ∑ 1/i.
    1/1 + 1/2 + 1/3 + 1/4 + ... + 1/n

    Exercise R-4.6, Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.
    :param n:
    :return: nth harmonic number.

    """

    # the 1st harmonic number is 1...
    if n == 1:
        return 1
    return 1/n + harmonic_number(n-1)


def str_to_integer(string):
    """
    Recursive function for converting a string of digits into the integer it represents.
    For example, 13531 represents the integer 13,531.

    Works by recursively chopping off the end and multiplying by 10.

    Exercise R-4.7, Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.
    :param string: String representation of the number.
    :return: integer representation.
    """
    n = len(string)
    if n == 0:
        return 0

    if string[0] == '-':
        return -1 * str_to_integer(string[1:n])

    return int(string[0]) * (10 ** (n-1)) + str_to_integer(string[1:n])


def towers_of_hanoi():
    """
    In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
    b, and c, sticking out of it. On peg a is a stack of n disks, each larger
    than the next, so that the smallest is on the top and the largest is on the
    bottom. The puzzle is to move all the disks from peg a to peg c, moving one
    disk at a time, so that we never place a larger disk on top of a smaller
    one. See Figure 4.15 for an example of the case n = 4. Describe a recursive
    algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (Hint:
    Consider first the sub-problem of moving all but the nth disk from peg a to
    another peg using the third as “temporary storage.”)

    Exercise R-4.14, Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.
    """
    # TODO: towers of hanoi


def is_palindrome(string):
    """
    Short recursive Python function that determines if a string s is a
    palindrome, that is, it is equal to its reverse. For example, 'racecar'
    and 'gohangasalamiimalasagnahog' are palindromes.

    Exercise R-4.17, Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.
    :return:
    """
    n = len(string)
    if n < 2:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])


def count_vowels_and_consonants(string):
    """
    Recursive function for counting vowels than consonants in a string.
    :return:
    """
    if type(string) is not str:
        raise TypeError
    n = len(string)
    if n == 0:
        return 0, 0

    v, c = count_vowels_and_consonants(string[1:n])

    if string[0] in ('a', 'i', 'e', 'o', 'u'):
        return v + 1, c
    elif string[0].isalpha():
        return v, c + 1
    else:
        return v, c


def more_vowels_or_consonants(string):
    """
    Recursive function for determining if a string s has more vowels than consonants.

    Exercise R-4.18, Chapter 4, Data Structures and Algorithms in Python, Goodrich et al.
    :return:
    """
    # TODO: complete vowels and consonants count.


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
