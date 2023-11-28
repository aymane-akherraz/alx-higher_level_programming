#!/usr/bin/python3
def remove_char_at(str, n):
    cp = ""
    if n < 0 or n > (len(str) - 1):
        return (str)
    cp = str[:n] + str[n+1:]
    return (cp)
