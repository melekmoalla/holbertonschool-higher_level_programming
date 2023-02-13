#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base:
"""

class Rectangle(Base):
    """
    * In the file models/rectangle.py
    * Class Rectangle inherits from Base
    * Private instance attributes, each with
    its own public getter and setter:
        - __width -> width
        - __height -> height
        - __x -> x
        - __y -> y
    * Class constructor: def
    __init__(self, width, height, x=0, y=0, id=None):
    * Call the super class with id - this super call
     with use the logic of the __init__ of the Base class
    Assign each argument width, height, x and y to
     the right attribute
    """
    from models.base import Base

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def get_x(self):
        return (self._x)

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return (self, _y)

    def set_y(self, value):
        self._y = value
