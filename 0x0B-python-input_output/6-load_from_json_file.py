#!/usr/bin/python3
"""write a fuction that create an object from json file"""


import json


def load_from_json_file(filename):
    """create an object from JSON file"""
    with open(filename) as f:
        return json.loads(f)
