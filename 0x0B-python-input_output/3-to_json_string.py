#!/usr/bin/python3

'''Module that contains a function that returns the JSON
representation of an object

'''

import json

def to_json_string(my_obj):
    '''Return JSON representation of a string'''

    return json.dumps(my_obj)
