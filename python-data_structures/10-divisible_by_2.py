#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = ["", "", "", "", "", "", "", "", "", "",
         "", "", "", "", "", "", "", "", "", "", ""]
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            a[i] = True
        else:
            a[i] = False
    a=a[:len(my_list)]
    return (a)
