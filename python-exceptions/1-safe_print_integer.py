#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not value and value != 0:
            raise ValueError
        int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
