#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ln = len(tuple_a)
    ln2 = len(tuple_b)
    if ln < 2:
        tuple_a = tuple_a + (0,) * (2 - ln)
    elif ln2 < 2:
        tuple_b = tuple_b + (0,) * (2 - ln2)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
