#!/usr/bin/python3
'''a simple Rectangle'''


class Rectangle:
    '''Rectangle'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
    '''property'''
    @property
    def width(self):
        return self.__width
    '''setter'''
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__width = value
    '''property'''
    @property
    def height(self):
        return self.__height
    '''setter'''
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__height = value
    '''area'''
    def area(self):
        return self.__width * self.__height
    '''perimeter'''
    def perimeter(self):
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (self.__width + self.__height) * 2
    '''return #'''
    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            return ((str(self.print_symbol) * self.__width) + '\n') * (
                self.__height - 1) + (str(self.print_symbol) * self.__width)
        else:
            d = ""
            return d
    '''repr'''
    def __repr__(self):
        return "Rectangle(" + str(
            self.__width) + ", " + str(self.__height) + ")"
    '''del'''
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
