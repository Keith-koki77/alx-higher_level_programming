#!/usr/bin/python3

""" Defines a rectangle class """

class Rectangle:

    """ A class that defines a Rectangle """


    def __init__(self, width=0, height=0):

        """ Initializes a new reactangle


        Arguments:
                width(int): width of the new rectangle 
                height(int): height of the new rectangle

        """

        self.width = width
        self.height = height

    @property
    def width(self):

        """ Gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):

        """ Sets the width of the rectangle """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):

        """ Gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):

        """ Sets the height of the rectangle """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value


    def area(self):

        """ Returns the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):

        """ Return the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns printable representation of rectangle 

        Represents the rectangle with # character
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
