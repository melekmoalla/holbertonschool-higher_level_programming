#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0):
        return (my_list)
    if (len(my_list)-1 >= idx):
        a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(my_list)):
            a[i] = my_list[i]
            if (idx == i):
                a[i] = element

        return (a[0: len(my_list)])
    return (my_list)
