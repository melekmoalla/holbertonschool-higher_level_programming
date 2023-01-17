#!/usr/bin/python3
if __name__ == '__main__':
    """
    add add,sub,div,mul
    """
    from calculator_1 import add, sub, div, mul

    a = 10
    b = 5
    result1 = add(a, b)
    print("{} + {} = {}".format(a, b, result1))
    result2 = sub(a, b)
    print("{} - {} = {}".format(a, b, result2))
    result4 = mul(a, b)
    print("{} * {} = {}".format(a, b, result4))
    result3 = div(a, b)
    print("{} / {} = {}".format(a, b, result3))
