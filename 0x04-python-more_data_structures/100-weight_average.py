#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s = 0
    s2 = 0
    for t in my_list:
        s += (t[0] * t[1])
        s2 += t[1]
    return (s / s2)
