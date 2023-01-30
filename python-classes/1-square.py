#!/usr/bin/python3
class Square:
    """
    Defines a square object with a size.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size: int):
        """
        The constructor for Square class.

        Parameters:
            size (int): The size of a side of the square.

        """
        self.__size = size
