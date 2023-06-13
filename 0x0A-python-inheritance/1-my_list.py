#!/usr/bin/python3

"""Defines an inherited list class Mylist"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """print sorted list"""
        res = list.copy(self)
        list.sort(res)
        print(res)
