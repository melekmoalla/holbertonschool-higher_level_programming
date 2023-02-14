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
