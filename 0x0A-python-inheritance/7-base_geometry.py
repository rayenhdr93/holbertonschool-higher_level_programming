#!/usr/bin/python3
"""method def"""


class BaseGeometry:
    """class def"""
    def area(self):
        """def area"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """def integer_validator"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
