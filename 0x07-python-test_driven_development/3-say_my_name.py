#!/usr/bin/python3

"""Module that prints a name"""


def say_my_name(first_name, last_name=""):

    """Prints the full anme in the format 'My name is <first name> <last name>.'


    Args:
        first_name (str): first name
        last_name (str, optional): last name. Defaults to an empty string

    Raises:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a sting

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = " ".join(filter(None, [first_name, last_name]))
    print("My name is", full_name)
