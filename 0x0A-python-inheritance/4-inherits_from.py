#!/usr/bin/python3
"""method def"""


def inherits_from(obj, a_class):
    """Method def"""
    return False if type(obj) is a_class else isinstance(obj, a_class)
