#!/usr/bin/python3

""" Defines a Rectangle class """


class Rectangle:

    """ A class that defines a Rectangle

    Args:
        width(int): width of the new rectangle.
        height(int): height of new rectangle

    """

    self.__width = width
    self.__height = height

    @property
    def width(self):

        """ Gets the width of the rectangle """

        return self.width

    @width.setter
    def width(self, value):

        """ sets the width of the rectangle """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.width = value

    @property
    def height(self):

        """ Gets the height of the rectangle """

        return self.height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.height = value


    def area(self):

        """ Returns the area of the rectangle """

        return self.width * self.height

    def perimeter(self):

        """Returns the perimeter of the rectangle """

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)
