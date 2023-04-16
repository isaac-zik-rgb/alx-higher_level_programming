#!/usr/bin/python3

"""Define a function that returns boolen if the obj is of
specified class"""


def is_kind_of_class(obj, a_class):
    """Args:
obj (any): of the specifed class
a_class (type): a specified class attribute
Returns:
if the obj is of specified class - True
otherwise False
"""
    if isinstance(obj, a_class):
        return True
    return False
