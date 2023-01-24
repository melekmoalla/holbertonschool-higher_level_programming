#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    sum = 0
    for i in range(len(my_list)):
        for j in range(i):
            if (my_list[i] == my_list[j]):
                a = 1
        if (a == 0):
            sum += my_list[i]
        a = 0
    return (sum)
