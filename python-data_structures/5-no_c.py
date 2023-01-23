#!/usr/bin/python3
def no_c(my_string):
    b = 0
    for i in range(len(my_string)):
        if ((ord(my_string[i]) == ord('c') or (ord(my_string[i]) == ord('C')))):
            if (b == 0):
                a = my_string[:i] + my_string[i+1:]
                b = 1
            else:
                a = a[:i] + a[i+1:]
    if (b == 1):
        return (a)
    else:
        return (my_string)
