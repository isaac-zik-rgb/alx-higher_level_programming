#!/usr/bin/python3
"""Defines a function that represents python object in json"""


import json


def from_json_string(my_str):
    """Return the python object json of str"""
    return json.loads(my_str)
