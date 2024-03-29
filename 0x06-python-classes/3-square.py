#!/usr/bin/python3
"""Define a Square"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):
        """Initializing a new Square.
Args:
size (init): the size of a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)
