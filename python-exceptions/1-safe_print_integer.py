#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not value:
            raise ValueError('empty string')
        int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
