#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is []:
        return my_list
    normalization = 0
    val = 0
    sum = 1
    for value in ((my_list)):
        sum = 1
        for a in ((value)):
            sum *= a
        val += sum
        normalization += a
    return (val / normalization)
