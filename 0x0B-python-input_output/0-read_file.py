#!/usr/bin/python3
'''Im bored of this des..'''


def read_file(filename=""):
    '''is it that important ?'''
    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
