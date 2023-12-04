#!/usr/bin/env python3
def no_c(my_string):
    chars = ['C', 'c']
    new_str = ""
    for i in my_string:
        if i not in chars:
            new_str += i
    return new_str
