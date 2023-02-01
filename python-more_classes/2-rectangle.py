#!/usr/bin/python3
""""
class Rectangle that defines a rectangle
- property def width(self): to retrieve it
- property setter def width(self, value): to set it:
    * width must be an integer, otherwise raise a TypeError
     exception with the message width must be an integer
    * if width is less than 0, raise a ValueError exception
     with the message width must be >= 0

- property def height(self): to retrieve it
- property setter def height(self, value): to set it:
    * height must be an integer, otherwise raise a TypeError
     exception with the message height must be an integer
    * if height is less than 0, raise a ValueError exception
     with the message height must be >= 0

"""


class Rectangle:

    """
    - Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * (self.__width + self.__height))
