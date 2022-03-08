#!/usr/bin/python3
'''a simple square'''


class Square:
    '''class definition'''
    def __init__(self, size=0):
        s = 1
        try:
            if type(size) is not int:
                s = s + 'f'
            if (size < 0):
                s = s / 0
        except TypeError:
            raise TypeError("size must be an integer")
        except ZeroDivisionError:
            raise ValueError("size must be >= 0")
        finally:
            self.__size = size
