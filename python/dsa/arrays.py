"""
arrays.py: Algorithms based on array operations.

Primarily from Chapter 5, Data Structures and Algorithms in Python, Goodrich et al.

"""

__author__ = 'nehar'

import ctypes

class DynamicArray(object):
    """
    Dynamic Array class.

    Implements a dynamic array based on the low level ctypes array.
    Section 5.1.3, Data Structures and Algorithms in Python, Goodrich et al.
    """

    def __init__(self):
        """
        Create an empty array.
        :return:
        """
        # actual count
        self._count = 0
        # maximum elements the raw array can hold
        self._capacity = 1

        # allocate capacity
        self._array = self._alloc(self._capacity)

    @staticmethod
    def _alloc(capacity):
        """
        Allocate array of specified capacity.
        :param capacity: capacity to allocate.
        :return: raw array
        """
        return (capacity * ctypes.py_object)()

    def __len__(self):
        """
        Return array length.

        :return:
        """
        return self._count

    def __getitem__(self, index):
        """
        Element access.

        :param index: index of element to access.
        :return: object at index.
        """

        # array index out of bounds
        if index < 0:
            index += self._count

        if not 0 <= index < self._count:
            raise IndexError("Invalid index")

        return self._array[index]

    def __repr__(self):
        """
        Object representation.
        :return: List representation.
        """

        try:
            return str([self._array[i] for i in range(self._count)])
        except ValueError as e:
            print(e)
            return str([])

    def append(self, item):
        """
        Add element to end of array.
        Array is doubled on attempt to append beyond capacity.

        :param item: Element to append
        :return: None
        """
        # resize
        if self._count == self._capacity:
            self._resize(2 * self._capacity)

        # append element
        self._array[self._count] = item

        self._count += 1

    def insert(self, k, item):
        """
        Insert value at index k.

        :param k: index to insert at.
        :param item: value to insert.
        :return: None
        """
        # resize to double capacity
        if self._count == self._capacity:
            self._resize(2 * self._capacity)

        # shift elements to the right...
        for j in range(self._count, k, -1):
            self._array[j] = self._array[j-1]

        # insert value at
        self._array[k] = item
        self._count += 1

    # TODO: implement array shrinking.
    def remove(self, value):
        """
        Removes  first occurrence of value.
        :param value: Value to remove.
        :return: None
        :raises ValueError: Raised if value is not found.
        """

        # look for a match
        for i in range(self._count):
            if self._array[i] == value:  # found match
                # shift elements towards the left
                for j in range(i, self._count - 1):
                    self._array[j] = self._array[j+1]
                self._array[self._count-1] = None # mark for GC
                self._count -= 1
                return
        raise ValueError("{} not found".format(value))

    def _resize(self, capacity):
        """
        Resize backing array to capacity.

        :param capacity:
        :return: None
        """
        # make a new array
        new_array = self._alloc(capacity)

        # copy existing elements over
        for i, item in enumerate(self._array):
            new_array[i] = item

        # replace old array
        self._array = new_array
        self._capacity = capacity


class CaesarCipher(object):
    """
    Implementation of the simple Caesar Cipher, a type of substitution cipher.

    Each letter in a message is replaced by a letter displaced by a fixed
    number of positions in the alphabet.

    Section 5.5.3, Data Structures and Algorithms in Python, Goodrich et al.
    """

    def __init__(self, shift):
        """
        Constructs Caesar cipher with specified rotation.

        Creates the encoding and decoding 'keys' as instance variables.

        :param shift: rotation integer value.
        """
        self._shift = shift

        # use temporary lists to avoid creating multiple string objects.
        e = [None] * 26
        d = [None] * 26

        # pre-compute encoding and decoding keys, based on ascii ordinal values.
        for i in range(26):
            e[i] = chr((i + shift) % 26 + ord('A'))
            d[i] = chr((i - shift) % 26 + ord('A'))

        self._enc_key = ''.join(e)
        self._dec_key = ''.join(d)

    def encrypt(self, message):
        """
        Encrypt message using pre-computed cipher.

        :param message: input message
        :return: encrypted message
        """
        return self._transform(message, self._enc_key)

    def decrypt(self, message):
        """
        Decrypt encrypted message using pre-computed cipher.

        :param message: encrypted message
        :return: decrypted message
        """
        return self._transform(message, self._dec_key)

    @staticmethod
    def _transform(message, key):
        """
        Transform input message based on key.
        :param message:
        :param key:
        :return:
        """

        # convert input to list to avoid creating multiple objects.
        temp = list(message)

        for i in range(len(temp)):
            if temp[i].isalpha():
                j = ord(temp[i].upper()) - ord('A')
                temp[i] = key[j]

        return ''.join(temp)

class MultiDimensional(object):
    """
    Multi dimensional array related exercises.

    Chapter 4 exercises, Data Structures and Algorithms in Python, Goodrich et al.
    """
    def compute_sum_std(self):
        """
        Uses standard control structures to compute the sum of all numbers in
        an n × n data set, represented as a list of lists.
        :return: sum of matrix elements.
        """

