#!/usr/bin/python3
"""A fuction that returns the dictionary description of simple
data structure"""


def class_to_json(obj):
    """Returns the dictionary description of simple data structure"""
    return obj.__dict__
