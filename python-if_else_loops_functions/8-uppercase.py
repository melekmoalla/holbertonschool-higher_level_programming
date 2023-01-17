#!/usr/bin/python3
def uppercase(string):
    for i in range(len(string)):
        if ord(string[i]) in range(97, 123):
            string = string[:i] + chr(ord(string[i])-32) + string[i+1:]
    print("{}\n".format(string))
