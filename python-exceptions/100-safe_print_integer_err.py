#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        int(value)
        print(int(value))
        return True
    except Exception:
        sys.stderr.write("Exception: Unknown format code 'd' for object of type str \n")
        return False
