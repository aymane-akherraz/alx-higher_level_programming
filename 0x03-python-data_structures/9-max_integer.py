#!/usr/bin/python3
def max_integer(my_list=[]):
    ln = len(my_list)
    if ln == 0:
        return
    m = my_list[0]
    for i in range(ln - 1):
        if m < my_list[i + 1]:
            m = my_list[i + 1]
    return m
