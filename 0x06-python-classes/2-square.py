#!/usr/bin/python3
"""define a Square"""


class Square:
    """Represent a class"""

    def __init__(self, size=0):
        """initializing a new square
Args:
size (init): The size of a new square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
