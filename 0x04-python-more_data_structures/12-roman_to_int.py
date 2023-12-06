#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    n = 0
    ln = len(roman_string)
    for i in range(ln):
        cur = roman_numerals[roman_string[i]]
        nxt = roman_numerals[roman_string[i + 1]] if (i + 1) < ln else 0
        if cur >= nxt:
            n += cur
        else:
            n -= cur
    return n
