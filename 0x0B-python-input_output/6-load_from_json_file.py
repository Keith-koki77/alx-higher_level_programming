#!/usr//bin/python3

'''Defines a JSON file-reading functiono'''
import json


def load_from_json_file(filename):
    '''creates an object from a json file'''
    with open(filename, 'r', encoding='utf-8') as fn:
        return json.load(fn)
