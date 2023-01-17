#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            if (i != len(str)-1):
                string = str[:i] + chr(ord(str[i])-32) + str[i+1:]
            else:
                string = str[:i] + chr(ord(str[i])-32)
    print("{}\n".format(string))
