#!/usr/bin/python3
"""
Write a function that returns True if the object
is an instance of a class that inherited 
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    Prototype: def inherits_from(obj, a_class)
    """

    if isinstance(obj, a_class):
        return(True)
    else:
        return(False)
