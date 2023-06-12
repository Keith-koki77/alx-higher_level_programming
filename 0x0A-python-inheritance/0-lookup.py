#!/usr/bin/python3

"""Returns the list of available attributes and methods"""

def lookup(obj):
    """Get the list of object attributes and methods"""
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    """Return the combined list of attributes and methods"""
    return attributes + methods
