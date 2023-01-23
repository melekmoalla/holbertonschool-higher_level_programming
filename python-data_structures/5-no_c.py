#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if ((ord(my_string[i]) == ord('c') or (ord(my_string[i]) == ord('C')))):
            a = my_string[:i] + my_string[i+1:]
    return (a)
