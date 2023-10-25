#!/usr/bin/python3
'''Definition of module'''
class Square:
    '''Definition of class'''
    def __init__(self, size=0):
        '''Try'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
