#!/usr/bin/python3
"""method def"""


from models.base import Base


class Rectangle(Base):
    """class def"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter"""
        return self.__width

    @property
    def height(self):
        """getter"""
        return self.__height

    @property
    def x(self):
        """getter"""
        return self.__x

    @property
    def y(self):
        """getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """def area"""
        return self.height * self.width

    def display(self):
        """def display"""
        for i in range(0, self.height + self.y):
            if i < self.y:
                print()
            else:
                for j in range(0, self.width + self.x):
                    if j < self.x:
                        print(" ", end="")
                    else:
                        print('#', end="")
                print()

    def __str__(self):
        '''def str'''
        str1 = "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/"
        str2 = str(self.y) + " - " + str(self.width) + "/" + str(self.height)
        return str1 + str2

    def update(self, *args, **kwargs):
        '''assigns an argument to each attribute'''
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """def to_dictionnary"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
