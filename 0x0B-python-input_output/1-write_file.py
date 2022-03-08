#!/usr/bin/python3
'''Im bored of this des..'''


def write_file(filename="", text=""):
    ''' is it that important u kiddin  '''
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)
        return len(text)
