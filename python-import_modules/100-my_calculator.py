#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
import sys
if __name__ == '__main__':
    """
    add add,sub,div,mul
    """
    if (len(sys.argv) - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if operator == "+":
        result = add(a, b)
        print("{} + {} = {}".format(a, b, result))
    elif operator == "-":
        result = sub(a, b)
        print("{} - {} = {}".format(a, b, result))
    elif operator == "*":
        result = mul(a, b)
        print("{} * {} = {}".format(a, b, result))
    elif operator == "/":
        result = div(a, b)
        print("{} / {} = {}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    