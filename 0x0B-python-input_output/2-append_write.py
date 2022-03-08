#!/usr/bin/python3
'''Im bored of this des..'''


def append_write(filename="", text=""):
    ''' is it that important u kiddin  '''
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
