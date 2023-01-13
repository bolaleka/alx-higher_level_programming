#!/usr/bin/python3
""" The Module is an operational method
    it operate with two argument and must be int type
    Cast any float type argument to int
    Return the additional of both args
"""


def add_integer(a, b=98):

    """add two integers
    Args:
    a (int): first param
    b (int): second param
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
