#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        a = fct(args[0], args[1])
        return(a)
    except:
        return(None)