#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    o_dictionary = {}
    for i in a_dictionary.keys():
        o_dictionary[i] = a_dictionary[i] * 2
    return o_dictionary
