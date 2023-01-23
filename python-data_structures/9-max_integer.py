#!/usr/bin/python3
def max_integer(my_list=[]):
    a = 0
    if (my_list == []):
        return (None)
    for i in range(len(my_list)):
        if (my_list[i] > a):
            a = my_list[i]
    return (a)
