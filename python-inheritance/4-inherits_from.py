#!/usr/bin/python3
"""
Write a function that returns True if the object
"""


def inherits_from(obj, a_class):
    """
    Prototype: def inherits_from(obj, a_class)
    """

    if isinstance(obj, a_class):
        return(True)
    else:
        return(False)
