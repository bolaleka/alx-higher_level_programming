#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    d = sorted(a_dictionary)
    i = 0
    for k, v in a_dictionary.items():
        print(d[i],': ', a_dictionary.get(d[i]))
        i += 1
