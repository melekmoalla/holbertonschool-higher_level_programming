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
        self.size = size

    def area(self):
        if not isinstance(self.size, int):
            raise TypeError("size must be an integer")
        if (self.size < 0):
            raise ValueError("size must be >= 0")
        return (self.size**2)
