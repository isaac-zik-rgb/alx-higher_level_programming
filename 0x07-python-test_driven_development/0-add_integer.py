#!/usr/bin/python3
#0-add_integer.py

"""Define an integer addition function"""
def add_integer(a, b=98):
    """float integers are first typecasted into ints before
addition is performed.

Raises:
TypeError: If either a or b is non-integer and non-float
"""
    if ((not isinstance(a, int) and not
         isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not
         isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
