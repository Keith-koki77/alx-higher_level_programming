#!/usr/bin/python3

"""Defines  a class MyInt that inherits an integer"""


class MyInt(int):

    """Invert int operator == and is != """

    def __eq__(self, value):
        """overide =="""

        return self.real != value

    def __ne__(self, value):
        """overide !="""
        
        return self.real == value

