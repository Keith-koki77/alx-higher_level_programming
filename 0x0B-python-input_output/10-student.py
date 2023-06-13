#!/usr/bin/python3

'''Defines a class student'''


class Student:
    '''Represents a student'''

    def __init__(self, first_name, last_name, age):
        '''Initializes a new student

        Args:
            first_name: first name
            last_name:last name
            age: age
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Dict representation of student

        Args:
            attrs (list): (optional) The attributes to represent
        '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
