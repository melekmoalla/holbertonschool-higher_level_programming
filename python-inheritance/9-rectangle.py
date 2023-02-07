#!/usr/bin/python3
"""
 class Rectangle that inherits from BaseGeometry

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Instantiation with width and height: def __init__(self, width, height):
    * width and height must be private. No getter or setter
    * width and height must be positive integers, validated
     by integer_validator
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        return (self.__height*self.__width)
