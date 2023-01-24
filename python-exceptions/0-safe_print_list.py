#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    p = 0
    for i in my_list:
        print(i, end="")
        p += 1
        if (p == x):
            print()
            return (i)
    print()
    return (i)
