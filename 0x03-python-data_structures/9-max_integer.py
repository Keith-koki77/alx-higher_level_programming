#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1 or my_list is None:
        return None
    max_num = my_list[0]
    for int in my_list:
        if int > max_num:
            max_num = int

    return max_num
