#!/usr/bin/python3

"""Define a class Rectangle"""


class Rectangle:
    """Representing a rectangle"""

    def __int__(self, width=0, height=0):
        """Initializing a class attribute Rectangle
Args:
width (int): The width of a rectangle
height (int): The height of a rectangle
"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width private attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for private heught attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height private attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the rectangle.
Representing the rectangle with the # character"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")

        return ("".join(rect))
