#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0
    for i in range(x):
        my_list[i]
        try:
            int(my_list[i])
            print(my_list[i], end='')
            count += 1
        except:
            print
    print()
    return count
