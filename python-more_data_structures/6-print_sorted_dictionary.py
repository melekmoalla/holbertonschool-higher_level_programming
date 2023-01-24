#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):

    sorted_dict = a_dictionary.keys()
    sorted_dict = sorted(sorted_dict)

    # Printing sorted dictionary
    for key in sorted_dict:
        print("{}: {}".format(key, a_dictionary[key]))
