#!/usr/bin/python3
"""Create class Square by checking an exception"""


class Square:
    """Define __init__ to instantiate a private
       instance attribute: size
    """

    def __init__(self, size=0):
        if int(size) >= 0 and isinstance(size, int) is True:
            self.__size = size
        elif int(size) >= 0:
            raise TypeError("size must be an intger")
        elif int(size) < 0 and isinstance(size, int) is True:
            raise ValueError("size must be >= 0")
    """define a square area"""
    def area(self):
        return self.__size * self.__size
