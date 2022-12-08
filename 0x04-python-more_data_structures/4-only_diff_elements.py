#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    list_1 = list(set_1)
    list_2 = list(set_2)
    new_list = []
    for j in list_1:
        if j not in list_2:
            new_list.append(j)
    for i in list_2:
        if i not in list_1:
            new_list.append(i)
    return new_list
