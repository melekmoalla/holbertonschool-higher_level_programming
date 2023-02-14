#!/usr/bin/python3
"""
Write the first class Base
"""
import json


class Base:
    """""
    * Create a file named models/base.py:
    * Class Base:
    * private class attribute __nb_objects = 0
    * class constructor: def __init__(self, id=None)::
        - if id is not None, assign the public instance
         attribute id with this argument value -
          you can assume id is an integer and you
           don’t need to test the type of it
        otherwise, increment __nb_objects and
        assign the new value to the public instance attribute id
    """""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
         the static method def to_json_string(list_dictionaries):
         that returns the JSON string representation of list_dictionaries:
            -   list_dictionaries is a list of dictionaries
            -   If list_dictionaries is None or empty, return
            the string: "[]"
            -   Otherwise, return the JSON string
            representation of list_dictionaries
        """
        if list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        the class method def save_to_file(cls, list_objs):
        that writes the JSON string representation of list_objs to a file:

            -list_objs is a list of instances who inherits of Base -
            example: list of Rectangle or list of Square instances
            -If list_objs is None, save an empty list
            -The filename must be: <Class name>.json - example:
            Rectangle.json
            -You must use the static method to_json_string (created before)
            -You must overwrite the file if it already exists
        """
        if list_objs is None:
            list_objs = []
        filname = cls.__name__+".json"
        with open(filname, "w") as f:
            listt = []
            for i in (list_objs):
                a = i.to_dictionary()
                listt.append(a)
            json_string = cls.to_json_string(listt)
            json.dump(listt, f)

    @staticmethod
    def from_json_string(json_string):
        """
        adding the static method def from_json_string(json_string):
        that returns the list of the JSON string representation json_string:

            -json_string is a string representing a list of dictionaries
            -If json_string is None or empty, return an empty list
            -Otherwise, return the list represented by json_string
        """
        if (json_string is None):
            return([])
        return (json.loads(json_string))
