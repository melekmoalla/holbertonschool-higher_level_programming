#!/usr/bin/python3
"""
Write a class Student that defines a student by:
"""


class Student:
    """
    * Public instance attributes:
        - first_name
        - last_name
        - age
    * Instantiation with first_name, last_name and age:
    * def __init__(self, first_name, last_name, age):
    * Public method def to_json(self, attrs=None): that retrieves
     a dictionary representation of a Student instance
     (same as 8-class_to_json.py):
        - If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            obj_dict = self.__dict__
            return (obj_dict)
        else:
            d = {}
            for at in attrs:
                if at == 'first_name':
                    d[at] = self.first_name
                if at == 'last_name':
                    d[at] = self.last_name
                if at == 'age':
                    d[at] = self.age
        return (d)
