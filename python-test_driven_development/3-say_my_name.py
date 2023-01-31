#!/usr/bin/python3
"""
    Function that print the first name and last name.
    first_name and last_name must be strings otherwise, raise a TypeError
    exception with the message first_name must be a string or last_name must
    be a string
    Returns an integer: My name is "+first_name+" "+last_name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that print the first name and last name.
    first_name and last_name must be strings otherwise, raise a TypeError
    exception with the message first_name must be a string or last_name must
    be a string
    Returns an integer: My name is "+first_name+" "+last_name
    """
    if type(first_name)not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name)not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is "+first_name+" "+last_name)
