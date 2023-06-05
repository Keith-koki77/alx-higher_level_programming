#!/usr/bin/python3

""" Defines a rectangle class """


class Rectangle:

    """ A class that defines a Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        """ Initializes a new reactangle


        Arguments:
                width(int): width of the new rectangle 
                height(int): height of the new rectangle

        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Return the rectangle with the greatest area

        Arguments:
                    rect_1: first rectangle
                    rect_2; second rectangle

        Raises:
                TypeError: if either rect_1 or rect_2 isn't a rectangle

        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

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

    def __repr__(self):
        """
        Returns the string representation of a rectangle 
        """
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        """ Prints a message for every deletion of a Rectangle """
        print("Bye rectangle...")
