#!/usr/bin/python3

def roman_to_int(roman_string):
    sum = 0
    if type(roman_string) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in roman_string:
        for a in roman_dict:
            if (a == i):
                sum += roman_dict[a]
    return sum
