#!/usr/bin/python3
"""
 class Rectangle that inherits from BaseGeometry

"""


class BaseGeometry:
    """
    * Public instance method: def area(self): that raises
    an Exception with the message area() is not implemented
    * def integer_validator(self, name, value):
        - you can assume name is always a string
        - if value is not an integer: raise a TypeError exception,
    with the message <name> must be an integer
       - if value is less or equal to 0: raise a ValueError
    exception with the message <name> must be greater than 0
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle:
    """
    Instantiation with width and height: 
    def __init__(self, width, height):
    """
    def __init__(self, width, height):
        self._width = width
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        self._height = height
        
