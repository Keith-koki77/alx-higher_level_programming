#!/usr/bin/python3

"""Defines a function that adds attributes to objects"""


def add_attribute(obj, att, value):
    """Adds a new attribute to object if possible

    Args:
        obj(any): object to add attribute to
        att(str): name of attribute to add obj to.
        value(any): value of attribute

    Raise:
        TypeError: if attribute notb added

    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
