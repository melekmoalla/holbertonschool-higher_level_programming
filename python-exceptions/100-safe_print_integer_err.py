#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    if value == None:
        sys.stderr.write(
            "Exception: unsupported format string passed to NoneType.__format__\n")
        return False
    if isinstance(value, list):
        sys.stderr.write(
            "Exception: unsupported format string passed to list.__format__\n")
        return False
    try:
        int(value)
        print("{:d}".format(value))
        return True

    except ValueError:
        if float(value).is_integer() == False:
            sys.stderr.write(
                "Exception: Unknown format code 'd' for object of type 'float'\n")
            return False
        else:
            sys.stderr.write(
                "Exception: Unknown format code 'd' for object of type 'str'\n")
            return False
    except TypeError:
        sys.stderr.write(
            "Exception: unsupported format string passed to set.__format__\n")
        return False
