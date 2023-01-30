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
    def __init__(self, size: int):
        self.__size = size
