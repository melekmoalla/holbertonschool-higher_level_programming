#!/usr/bin/python3
def multiple_returns(sentence):
    a = None
    b = 0
    if (sentence == ""):
        return (b, a)
    else:
        a = sentence[0]
        b = len(sentence)
        return (b, a)
