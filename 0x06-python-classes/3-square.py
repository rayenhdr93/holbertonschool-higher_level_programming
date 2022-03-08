#!/usr/bin/python3
'''a simple square'''


class Square:
    '''class def'''
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    '''Area def'''
    def area(self):
        return self.__size * self.__size
