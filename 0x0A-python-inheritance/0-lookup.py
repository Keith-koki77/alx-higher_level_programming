#!/usr/bin/python3

"""Returns the list of available attributes and methods"""

def lookup(obj):
    """Returns a list of an object's available attributes"""
    return(dir(obj))
