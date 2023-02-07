#!/usr/bin/python3

"""
Write a class Square that inherits from Rectangle
(9-rectangle.py). (task based on 10-square.py).
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    *Instantiation with size: def __init__(self, size)::
    *size must be private. No getter or setter
    *size must be a positive integer, validated by integer_validator
    *the area() method must be implemented
    """

    def __init__(self, size):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        if (size <= 0):
            raise ValueError("size must be greater than 0")
        self.__size = size

    def area(self):
        return (self.__size*self.__size)

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
