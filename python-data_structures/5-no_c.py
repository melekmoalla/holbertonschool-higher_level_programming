#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for i in my_string:
        if ((i != 'c') and (i != 'C')):
            a += i
    return (a)
