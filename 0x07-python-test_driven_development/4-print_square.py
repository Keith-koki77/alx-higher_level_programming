#!/usr/bin/python3

"""Module that prints squares"""


def print_square(size):

    """Prints a square with the  '#' of given size


    args:
        size(int): the size length of the square

    Raises:
        TypeError: if size is not an integer
        TypeError: if size is less than zero
        TypeError: if size is not a float and is less than zero.

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >=0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
