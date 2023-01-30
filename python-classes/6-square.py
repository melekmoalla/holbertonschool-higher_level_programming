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
        self.__size = size   
        self.__position = position 

    ''' retrieve size and make it private'''

    @property
    def size(self):
        return self.__size


    @property
    def position(self):
        return self.__position

    ''' set private size attribute '''
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position[0] = value[0]
        self.__position[1] = value[1]

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

