#!/usr/bin/python3
"""
Defines a square object with a size.

Attributes:
    __size (int): The size of a side of the square.
"""


class Square:

    ''' create Square instance with public attributes
    size and position '''

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    ''' retrieve size and make it private'''

    @property
    def size(self):
        return self.__size

    ''' set private size attribute '''

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if ((len(value)) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(
                value) != tuple or value[0] < 0 or value[1] < 0 or value[1] == "":
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    ''' calculates area of square '''

    def area(self):
        return self.__size ** 2

    ''' print of square '''

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for space in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print()
