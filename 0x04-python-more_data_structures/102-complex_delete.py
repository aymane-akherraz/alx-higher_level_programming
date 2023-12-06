#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_del = []
    for k, v in a_dictionary.items():
        if value in a_dictionary.values():
            if v == value:
                to_del.append(k)
        else:
            break
    for key in to_del:
        del a_dictionary[key]
    return a_dictionary
