#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    b = 0
    p = 0
    m = 0
    a = 0
    if (len(tuple_b) > 0):
        a = tuple_b[0]
    if (len(tuple_b) > 1):
        p = tuple_b[1]
    if (len(tuple_a) > 0):
        b = tuple_a[0]
    if (len(tuple_a) > 1):
        m = tuple_a[1]
    return (a+b, m+p)
