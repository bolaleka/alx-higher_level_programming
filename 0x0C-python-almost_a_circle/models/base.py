#!/usr/bin/python3

""" This is a base class"""


class Base:
    
    """define private class attribute
       and constructor
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """ init method to manipulate id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
