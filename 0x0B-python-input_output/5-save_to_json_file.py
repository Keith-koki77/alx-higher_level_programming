#!/usr/bin/python3

'''writes function on text file'''
import json

def save_to_json_file(my_obj, filename):
    '''write an object to a text file using JSON rpresentation'''
    with open(filename, 'w', encoding='utf-8') as fn:
        json.dump(my_obj, fn)
