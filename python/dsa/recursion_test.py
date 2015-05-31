"""
recursion_test.py: Test cases for recursion algorithms.
"""

__author__ = 'nehar'

import unittest
from recursion import factorial
from recursion import Ruler
from recursion import binary_search
from recursion import sum_linear
from recursion import sum_binary
from recursion import recursive_reverse
from recursion import naive_power
from recursion import recurrence_power
from recursion import find_max
from recursion import find_min_max
from recursion import product
from recursion import harmonic_number
from recursion import str_to_integer
from recursion import towers_of_hanoi
from recursion import is_palindrome
from recursion import count_vowels_and_consonants


class TestRecursion(unittest.TestCase):

    def test_factorial(self):
        """
        Test recursive factorial implementation.
        """
        self.assertEquals(1, factorial(0))
        self.assertEquals(1, factorial(1))
        self.assertEquals(2, factorial(2))
        self.assertEquals(6, factorial(3))
        self.assertEquals(3628800, factorial(10))
        self.assertEquals(1307674368000, factorial(15))

        # TODO: fails under python 2.7 - ValueError not raised :(
        with self.assertRaises(ValueError):
            factorial(3/2)
        with self.assertRaises(ValueError):
            factorial(-4)

    def test_ruler(self):
        """

        :return:
        """
        x = "---- 0\n-\n--\n-\n---\n-\n--\n-\n---- 1\n-\n--\n-\n---\n-\n--\n-\n---- 2\n"
        self.assertEquals(x, Ruler(inches=2, major_length=4).draw())
        print("\n\n"*5)

        x = "----- 0\n-\n--\n-\n---\n-\n--\n-\n----\n-\n--\n-\n---\n-\n--\n-\n----- 1\n"
        self.assertEquals(x, Ruler(inches=1, major_length=5).draw())
        print("\n\n"*5)

        x = """--- 0\n-\n--\n-\n--- 1\n-\n--\n-\n--- 2\n-\n--\n-\n--- 3\n"""
        self.assertEqual(x, Ruler(inches=3, major_length=3).draw())

    def test_binary_search(self):
        """
        Test recursive Binary search.
        :return:
        """
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5, 0, 5))
        self.assertTrue(binary_search([11, 12, 13, 15, 20], 11, 0, 5))

    def test_sum_linear(self):
        """
        Test Linear recursive sum of sequence.

        :return:
        """
        self.assertEquals(0, sum_linear())
        self.assertEquals(0, sum_linear([]))
        self.assertEquals(1, sum_linear([1]))
        self.assertEquals(3, sum_linear([1, 2]))
        self.assertEquals(6, sum_linear([1, 2, 3]))

    def test_sum_binary(self):
        """

        :return:
        """
        self.assertEquals(0, sum_binary())
        self.assertEquals(0, sum_binary([]))
        self.assertEquals(1, sum_binary([1]))
        self.assertEquals(3, sum_binary([1, 2]))
        self.assertEquals(6, sum_binary([1, 2, 3]))

    def test_recursive_reverse(self):
        """
        Test linear recursion based reverse.

        :return:
        """
        self.assertEquals([], recursive_reverse())
        self.assertEquals([1], recursive_reverse([1]))
        self.assertEquals([2, 1], recursive_reverse([1, 2]))
        self.assertEquals([3, 2, 1], recursive_reverse([1, 2, 3]))
        self.assertEquals([8, 7, 6, 5, 4, 3, 2, 1],
                          recursive_reverse([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEquals([5, 9, 8, 2, 6, 3, 4],
                          recursive_reverse([4, 3, 6, 2, 8, 9, 5]))

    def test_find_max(self):
        """
        Test recursive find_max.

        :return:
        """
        self.assertEquals(1, find_max([1]))
        self.assertEquals(10, find_max([5, 10, 1]))
        self.assertEquals(-1, find_max([-10, -20, -1]))
        with self.assertRaises(TypeError):
            self.assertEquals(1, find_max([]))
        self.assertEquals(0, find_max([0]))

    def test_find_min_max(self):
        """
        Test recursive find_min_max.

        :return:
        """
        with self.assertRaises(TypeError):
            find_min_max()
        with self.assertRaises(TypeError):
            find_min_max([])

        self.assertEquals((1, 1), find_min_max([1]))
        self.assertEquals((1, 2), find_min_max([2, 1]))
        self.assertEquals((1, 3), find_min_max([2, 1, 3]))
        self.assertEquals((-1, 2), find_min_max([2, -1, 1]))
        self.assertEquals((-1, 200), find_min_max([2, -1, 10, 3, 200]))
        self.assertEquals((-1, 200), find_min_max([2, -1, 1, 3, 200]))
        self.assertEquals((-1, 200), find_min_max([2, 1, -1, 3, 200]))
        self.assertEquals((-2, 3), find_min_max([-2, 1, -1, 3, 1]))

    def test_product(self):
        """
        Test recursive product function.
        """
        self.assertEqual(1, product(1, 1))
        self.assertEqual(2, product(2, 1))
        self.assertEqual(30, product(3, 10))
        self.assertEqual(33, product(3, 11))
        self.assertEqual(15, product(5, 3))
        self.assertEqual(0, product(3, 0))

        with self.assertRaises(TypeError):
            product(-15, 2)
        with self.assertRaises(TypeError):
            product(3.5, 10)
        with self.assertRaises(TypeError):
            product(5, 3.1)

    def test_naive_power(self):
        """
        Test naive recursive power function implementation.
        """
        self.assertEquals(1, naive_power(2, 0))
        self.assertEquals(2, naive_power(2, 1))
        self.assertEquals(4, naive_power(2, 2))
        self.assertEquals(-1, naive_power(-1, 1))
        self.assertEquals(27, naive_power(3, 3))
        self.assertEquals(-27, naive_power(-3, 3))

    def test_recurrence_power(self):
        """
        Test naive recursive power function implementation.
        """
        self.assertEquals(1, recurrence_power(2, 0))
        self.assertEquals(2, recurrence_power(2, 1))
        self.assertEquals(4, recurrence_power(2, 2))
        self.assertEquals(-1, recurrence_power(-1, 1))
        self.assertEquals(27, recurrence_power(3, 3))
        self.assertEquals(-27, recurrence_power(-3, 3))

    def test_harmonic_number(self):
        """
        Test recursive implementation of harmonic number calculation.
        """
        self.assertEquals(1, harmonic_number(1))
        self.assertEquals(3/2, harmonic_number(2))
        self.assertEquals(11/6, harmonic_number(3))

        # TODO: fails under python 2.7 :(
        self.assertEquals(round(25/12, 2), round(harmonic_number(4), 2))
        self.assertEquals(round(137/60, 2), round(harmonic_number(5), 2))

    def test_str_to_integer(self):
        self.assertEquals(0, str_to_integer("0"))
        self.assertEquals(1, str_to_integer("1"))
        self.assertEquals(2, str_to_integer("2"))
        self.assertEquals(1345, str_to_integer("1345"))
        self.assertEquals(13531, str_to_integer("13531"))

        self.assertEquals(-12, str_to_integer("-12"))
        self.assertEquals(-1, str_to_integer("-1"))
        self.assertEquals(-146444, str_to_integer("-146444"))

        with self.assertRaises(ValueError):
            str_to_integer("oogabooga")

        # TODO: this will fail right now as we don't have a syntax check.
        # self.assertEquals(1-46444, str_to_integer("1-46444"))

    def test_towers_of_hanoi(self):
        """

        :return:
        """

        self.assertEquals(None, towers_of_hanoi(n=1, source=[], middle=[], target=[]))
        with self.assertRaises(ValueError):
            towers_of_hanoi(n=1, source=None, middle=[], target=[])
        with self.assertRaises(ValueError):
            towers_of_hanoi(n=2, source=[], middle=None, target=[])
        with self.assertRaises(ValueError):
            towers_of_hanoi(n=3, source=[], middle=[], target=None)

        source = [1]
        middle = []
        target = []
        towers_of_hanoi(n=3, source=source, middle=middle, target=target)
        self.assertEquals([], source)
        self.assertEquals([1], target)
        self.assertEquals([], middle)

        source = [1, 2, 3]
        middle = []
        target = []
        towers_of_hanoi(n=3, source=source, middle=middle, target=target)
        self.assertEquals([], source)
        self.assertEquals([1, 2, 3], target)
        self.assertEquals([], middle)

        source = [4, 5, 6, 10]
        middle = []
        target = []
        towers_of_hanoi(n=3, source=source, middle=middle, target=target)
        self.assertEquals([], source)
        self.assertEquals([4, 5, 6, 10], target)
        self.assertEquals([], middle)

    def test_is_palindrome(self):
        """
        Test recursive is_palindrome.
        """
        self.assertTrue(is_palindrome("DABCBAD"))
        self.assertFalse(is_palindrome("AB"))
        self.assertTrue(is_palindrome("ABCBA"))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("gohangasalamiimalasagnahog"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("snap&stop"))

    def test_count_vowels_and_consonants(self):
        """
        Test recursive volwels & consonants count.
        """
        self.assertEquals((1, 2), count_vowels_and_consonants("abc"))
        self.assertEquals((2, 3), count_vowels_and_consonants("nehar"))
        self.assertEquals((0, 0), count_vowels_and_consonants("123"))
        self.assertEquals((1, 1), count_vowels_and_consonants("1a2B3"))
        self.assertEquals((0, 0), count_vowels_and_consonants(""))
        with self.assertRaises(TypeError):
            count_vowels_and_consonants([1, 2])
