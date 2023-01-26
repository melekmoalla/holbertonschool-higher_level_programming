#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    a = "Exception: unsupported format string passed to NoneType.__format__"
    b = "Exception: Unknown format code 'd' for object of type 'float'"
    c = "Exception: Unknown format code 'd' for object of type 'str'"
    if value is None:
        print("{}".format(a), file=sys.stderr)
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
        if float(value).is_integer() is False:
            print("{}".format(b), file=sys.stderr)
            return False
        else:
            print("{}".format(c), file=sys.stderr)
            return False
    except TypeError:
        sys.stderr.write(
            "Exception: unsupported format string passed to set.__format__\n")
        return False
