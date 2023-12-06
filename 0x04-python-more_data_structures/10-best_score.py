#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) or len(a_dictionary):
        return max(a_dictionary)
    return None
