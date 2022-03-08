#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    o_dictionary = list(sorted(a_dictionary.items()))
    for i in range(0, len(o_dictionary)):
        print(o_dictionary[i][0], end=": ")
        print(o_dictionary[i][1])
