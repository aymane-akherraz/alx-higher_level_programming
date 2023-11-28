#!/usr/bin/python3
def uppercase(str):
    ec, i, length = "", 0, (len(str) - 1)
    for c in str:
        if i == length:
            ec = "\n"
        if 97 <= ord(c) <= 122:
            print(chr(ord(c) - 32), end=ec)
        else:
            print(c, end=ec)
        i += 1
