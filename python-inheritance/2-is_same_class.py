#!/usr/bin/python3
"""
a function that returns True if the object is exactly
 an instance of the specified class ; otherwise False.
Prototype: def is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """
    Prototype: def is_same_class(obj, a_class):
    """
    if (type(obj) == a_class):
        return (True)
    else:
        return (False)
