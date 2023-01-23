#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0):
        return (None)
    for i in range(len(my_list)):
        if (idx == my_list[i]):
            return (idx+1)
    return (None)
