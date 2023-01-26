#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    if (len(args) == 0):
        a = fct()
        return (a)
    try:
        a = fct(args[0], args[1])
        return (a)
    except ZeroDivisionError as i:
        print(f"Exception: {i}", file=sys.stderr)
        return (None)

    except:
        print(f"Exception: list index out of range", file=sys.stderr)
        return (None)
