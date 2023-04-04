#!/usr/bin/python3

"""Define a class"""


class Rectangle:

    """Representing a class"""

    def __init__(self, width=0, height=0):
        """initializing a class instant"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instant
attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute wodth"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter a private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter a private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
