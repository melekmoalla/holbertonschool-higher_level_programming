#!/usr/bin/python3

class Rectangle:

    def __init__(self, width, height):
        self._width = width
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        self._height = height
        
