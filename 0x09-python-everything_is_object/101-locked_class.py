#!/usr/bin/python3

"""Module that prevents dynamic attributes creation"""


class LockedClass():
    """Class to prevent dyanamic attributes creation"""

    __slots__ = ['first_name']

    def __init__(self):
        """init method"""
        pass
