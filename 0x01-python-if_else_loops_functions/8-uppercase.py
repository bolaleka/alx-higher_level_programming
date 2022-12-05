#!/usr/bin/python3

def uppercase(str):
    res = ''
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            res += chr(ord(c) - 32)
        else:
            res += c
    print("{:s}".format(res))
