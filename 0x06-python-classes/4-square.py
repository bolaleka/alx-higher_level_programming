#!/usr/bin/python3
"""Create class Square by checking an exception"""


class Square:

    """Create init method"""
    def __init__(self, size=0):
        self.__size = size

    """Create getter method with private instance"""
    @property
    def size(self):
        return self.__size

    """Create setter method with private instance"""
    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    """define a square area"""
    def area(self):
        return self.__size ** 2
