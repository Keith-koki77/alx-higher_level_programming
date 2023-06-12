#!/usr/bin/python3

"""Defines a base geometry clas BaseGeometry"""

class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer

        Args:
            name(str): The anme of the parameter
            value(init): The parametr to validate

        Raises:
            TypeError: if value isn't an integer.
            ValueError: i9f value <= 0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
