#!/usr/bin/python3
"""
the class Square that inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    * In the file models/square.py
    *  Class Square inherits from Rectangle
    * Class constructor: def __init__(self, size, x=0, y=0, id=None):
    * Call the super class with id, x, y, width and height - this
     super call will use the logic of the __init__ of the Rectangle
    class. The width and height must be assigned to the value of size
    * You must not create new attributes for this class, use all attributes
    of Rectangle - As reminder: a Square is a Rectangle with the same
    width and height
    * All width, height, x and y validation must inherit
    from Rectangle - same behavior in case of wrong data
    * The overloading __str__ method should return
    * [Square]   (<id>) <x>/<y> - <size> - in our case, width or height
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        * the public method def update(self, *args, **kwargs)
        that assigns attributes:

        *args is the list of arguments - no-keyworded arguments
            - 1st argument should be the id attribute
            - 2nd argument should be the size attribute
            - 3rd argument should be the x attribute
            - 4th argument should be the y attribute
    **kwargs can be thought of as a double pointer to a dictionary:
     key/value (keyworded arguments)
    **kwargs must be skipped if *args exists and is not empty
    Each key in this dictionary represents an attribute to the instance
        """
        values = {
            "size": self.size,
            "id": self.id,
            "x": self.x,
            "y": self.y,
        }
        a = 0
        for i in args:
            if (a == 0):
                self.id = i
            if (a == 1):
                self.size = i
            if (a == 2):
                self.x = i
            if (a == 3):
                self.y = i
            a += 1

        for b in kwargs:
            for m in values:
                if (b == m):
                    values[m] = kwargs[b]
            self.id = values['id']
            self.size = values['size']
            self.x = values['x']
            self.y = values['y']

    def to_dictionary(self):
        """
        * the public method def to_dictionary(self):
        that returns the dictionary representation of a Square:

            - This dictionary must contain:

            - id
            - size
            - x
            - y
        """
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
