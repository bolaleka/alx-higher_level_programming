#!/usr/bin/python3

def common_elements(set_1, set_2):
    set1 = set(set_1)
    set2 = set(set_2)
    if (set1 & set2) is not None:
        return set1 & set2
