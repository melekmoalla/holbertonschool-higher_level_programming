#!/usr/bin/python3
"""
* Create a function def pascal_triangle(n): that
 returns a list of lists of
 integers representing the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    * Returns an empty list if n <= 0
    * You can assume n will be always
    an integer
    """
    if (n < 0):
        return []
    my_list = []
    for line in range(1, n+1):
        C = 1  # used to represent C(line, i)
        mylist2 = []
        for i in range(1, line + 1):
            # The first value in a
            # line is always 1
            mylist2.append(C)
            C = int(C * (line - i) / i)
        my_list.append(mylist2)

    return (my_list)
