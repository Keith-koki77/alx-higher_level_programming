#!/usr/bin/python3

"""Defines a rRectangle subclass Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Represents a square"""

    def __init__(self, size):
        """Initialize new square

        args:
             size(int): size of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
