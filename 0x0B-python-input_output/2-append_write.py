#!/usr/bin/python3

'''Fuinction that appends to a text file'''


def append_write(filename="", text=""):
    '''Function thatappends to a text file

    Args:
        filename(string): filename to append to.
        text(string): text to append filename to.

    Return: 
        Number of characters appended
    '''
    with open(filename, 'a', encoding='utf-8') as fn:
        return fn.write(text)
