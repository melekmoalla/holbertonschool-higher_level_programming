#!/usr/bin/python3
"""
    * function that prints a text with 2 new lines after each 
     of these characters: ., ? and :
    * Prototype: def text_indentation(text):
    * text must be a string, otherwise raise a TypeError
     exception with the message text must be a string
    * There should be no space at the beginning or at the end
     of each printed line
"""


def text_indentation(text):
    """
    * function that prints a text with 2 new lines after each 
     of these characters: ., ? and :
    * Prototype: def text_indentation(text):
    * text must be a string, otherwise raise a TypeError
     exception with the message text must be a string
    * There should be no space at the beginning or at the end
     of each printed line
    """
    if isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if (i == "?" or i == "." or i == ":"):
            print('\n')
        else:
            print(i,end="")


        
