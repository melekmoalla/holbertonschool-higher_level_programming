#!/usr/bin/python3
def common_elements(set_1, set_2):
    a = ""
    if (set_1 == set_2):
        a = set_1
        return (a)
    for i in set_1:
        for f in set_2:
            if (i == f):
                a = i
    return (a)
