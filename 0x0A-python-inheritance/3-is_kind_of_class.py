#!/usr/bin/python

"""Module that defines class and an inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """"Check if an object is an instance or inherited instance of class
    Args:
        obj: object to be checked
        a_class: class to match the type of object to

    Return:
        True: object is an instance of
        False: otherwise.
    """

    if isinstance(obj, a_class):
        return True
    return False
