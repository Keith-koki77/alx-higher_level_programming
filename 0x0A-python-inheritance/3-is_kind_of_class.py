#!/usr/bin/python3

"""Module that defines class and an inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """"Check if an object is an instance or inherited instance of class
    Args:
        obj: object to be checked
        a_class: class to match the type of object to
    """

    return isinstance(obj, a_class)
