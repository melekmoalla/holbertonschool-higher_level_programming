#!/usr/bin/python3
for i in range(9):
    for j in range(i+1, 9+1):
        if i != j and  i < 8:
            print(str(i)+str(j), end=", ")
        else:
            print(str(i)+str(j), end="\n")
