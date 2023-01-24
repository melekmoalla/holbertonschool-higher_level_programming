#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    sorted_dict = {}
    for key in a_dictionary:
        sorted_dict[key] = a_dictionary[key] * 2
    return(sorted_dict)
