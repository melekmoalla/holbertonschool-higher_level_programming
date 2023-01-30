#!/usr/bin/python3
"""
Defines a square object with a size.

Attributes:
    __size (int): The size of a side of the square.
"""


class Square:

    ''' create Square instance with public attributes
    size and position '''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    ''' calculates area of square '''

    def area(self):
        return self.__size ** 2

    ''' print of square '''

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.size):
                for i in range(self.size):
                    print('#', end="")
                print()
