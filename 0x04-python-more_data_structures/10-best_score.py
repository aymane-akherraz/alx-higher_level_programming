#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key = None
    max_v = 0
    for k, v in a_dictionary.items():
        if v > max_v:
            max_v = v
            key = k
    return key
