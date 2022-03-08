#!/usr/bin/python3
def uniq_add(my_list=[]):
    x = 0
    l_list = set(my_list)
    for ar in l_list:
        x += ar
    return x
