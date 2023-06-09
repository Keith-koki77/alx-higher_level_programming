#!/usr/bin/python3

"""Defines a base geometry clas BaseGeometry"""

class BaseGeometry:
    """Represent base geometry"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """another useless function"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
