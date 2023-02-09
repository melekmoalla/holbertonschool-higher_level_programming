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
    def __init__(self, first_name, last_name, age):
    * Public method def to_json(self):
    that retrieves a dictionary representation
    of a Student instance (same as 8-class_to_json.py)
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        obj_dict = self.__dict__
        return (obj_dict)
