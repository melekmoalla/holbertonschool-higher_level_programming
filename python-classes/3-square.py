#!/usr/bin/python3
"""
Defines a square object with a size.

Attributes:
    __size (int): The size of a side of the square.
"""


class Square:

    """
    The constructor for Square class.

    Parameters:
        size (int): The size of a side of the square.

    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size**2)
