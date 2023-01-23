#!/usr/bin/python3
def search_replace(my_list, search, replace):
    matr = [0 for j in range(len(my_list))]
    for i in range(len(my_list)):
        if (my_list[i] != search):
            matr[i] = my_list[i]
        else:
            matr[i] = replace
    return (matr)
