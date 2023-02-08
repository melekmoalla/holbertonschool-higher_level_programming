#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8)
and prints it to stdout
"""


def read_file(filename=""):
    """
    * Prototype: def read_file(filename=""):
    * You must use the with statement
    * You don’t need to manage file permission or
    file doesn't exist exceptions.
    """
    with open(filename, encoding='utf-8') as name_files:
        print(name_files.read(), end="")
        name_files.close()
