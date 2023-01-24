#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    b = None
    if (a_dictionary == None):
        return None
    for key in a_dictionary:
        if (a_dictionary[key] > a):
            a = a_dictionary[key]
            b=key
            
    return (b)
