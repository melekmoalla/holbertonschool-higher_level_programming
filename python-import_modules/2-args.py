#!/usr/bin/python3
import sys
if __name__ == '__main__':
    if (len(sys.argv)-1) == 0:
        print("0 arguments.")
    elif (len(sys.argv)-1) == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv)-1))
    for idx, arg in enumerate(sys.argv):
        if idx == 0:
            continue
        else:
            print("{}: {}".format(idx, arg))
