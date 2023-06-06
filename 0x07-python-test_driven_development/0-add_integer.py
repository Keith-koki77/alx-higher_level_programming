#!/usr/bin/python3

"""Module that contains addition operation function"""


def add_integer(a, b=98):
    """This function returns the addition of 2 arguments
    Args:
        a([int, float]): first number
        b([int, float]): second number

    Returns:
            Addition of two numbers
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
