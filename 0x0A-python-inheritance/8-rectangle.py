#!/usr/bin/python3

"""Define a class Rectangle that inherist from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representing a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer__validator("width", width)
        self.__width = width
        self.integer__validator("height", height)
        self.__height = height
