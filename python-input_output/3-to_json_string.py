#!/usr/bin/python3

"""
Write a function that returns the JSON
representation of an object (string):
"""


def to_json_string(my_obj):
    import json
    """
    * Prototype: def to_json_string(my_obj):
    * You don’t need to manage exceptions if the object can’t be
     serialized.
    """
    return json.dumps(my_obj)
