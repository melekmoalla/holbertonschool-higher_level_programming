#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """
    * In the file models/rectangle.py
    * Class Rectangle inherits from Base
    * Private instance attributes, each with
    its own public getter and setter:
        - __width -> width
        - __height -> height
        - __x -> x
        - __y -> y
    * Class constructor: def
    __init__(self, width, height, x=0, y=0, id=None):
    * Call the super class with id - this super call
     with use the logic of the __init__ of the Base class
    Assign each argument width, height, x and y to
     the right attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def _validate_integer_1(self, name, value):
        """
        verification for the value if is int and possitive
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be > 0")

    def _validate_integer_2(self, name, value):
        """
        verification for the value if is int and possitive
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self._validate_integer_1("height", value)
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self._validate_integer_1("width", value)
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self._validate_integer_2("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self._validate_integer_2("y", value)
        self.__y = value

    def area(self):
        """
        the public method def area(self):
         that returns the area value of the Rectangle instance.
        """
        return (self.__height*self.__width)

    def display(self):
        """
        * the public method def display(self):
        to print in stdout the Rectangle instance with
         the character # by taking care of x and y

        """
        for o in range(self.y):
            print()
        for i in range(self.height):
            for b in range(self.x):
                print(" ", end="")
            for a in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        p = self.width
        m = self.height
        a = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                    self.y, p, m)
        return (a)

    def update(self, *args, **kwargs):
        """
        * the prototype to update(self, *args, **kwargs)
        that assigns a key/value argument to attributes:

            - **kwargs can be thought of as a double
            pointer to a dictionary: key/value
            - As Python doesn’t have pointers,
            **kwargs is not literally a double pointer
            – describing it as such is just a way of explaining
            its behavior in terms you’re already familiar with
            -   **kwargs must be skipped if *args exists and is not empty
            - Each key in this dictionary represents an
            attribute to the instance
        """
        a = 0
        for arg in kwargs:
            if (arg == 'id'):
                self.id = kwargs[arg]
            if (arg == 'width'):
                self.width = kwargs[arg]
            if (arg == 'height'):
                self.height = kwargs[arg]
            if (arg == 'x'):
                self.x = kwargs[arg]
            if (arg == 'y'):
                self.y = kwargs[arg]
