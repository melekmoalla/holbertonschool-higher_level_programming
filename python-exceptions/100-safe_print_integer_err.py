#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    if value == None:
        sys.stderr.write(
            "Exception: unsupported format string passed to NoneType.__format__\n")
        return False
    try:
        int(value)
        print("{:d}".format(value))
        return True

    except IndexError:
        sys.stderr.write(
            "Exception: Unknown format code 'd' for object of type str \n")
        return False
    except ValueError:
        sys.stderr.write(
            "Exception: Unknown format code 'd' for object of type 'str'\n")
        return False
    except TypeError:
        print(" Exception: unsupported format string passed to set.__format__")
        return False
    except Exception:
        sys.stderr.write(
            "Exception: unsupported format string passed to set.__format__\n")
        return False
