#!/usr/bin/python3
def common_elements(set_1, set_2):
    unique = []
    for i in set_1:
        if i in set_2:
            unique.append(i)
            unique_set = set(unique)
    return unique_set

