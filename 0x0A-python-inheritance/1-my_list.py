#!/usr/bin/python3

"""Defines an inherited list class Mylist"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """print sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
