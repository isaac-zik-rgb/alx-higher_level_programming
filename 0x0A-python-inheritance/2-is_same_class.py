#!/usr/bin/python3

"""Define a function that returns true if the obj is an
instance of a specified class"""


def is_same_class(obj, a_class):
    """Args:
obj (any): an obj of a specified class
a_class (type): a class that match the type of obj to.
Returns:
if obj is exactly an instance of a_class - True
otherwise - False
"""
    if (type(obj) == a_class):
        return True
    return False
