#!/usr/bin/env python3
def print_last_digit(number):
    last_digit = int(repr(number)[-1])
    print(f"{last_digit}", end="")
    return(last_digit)
