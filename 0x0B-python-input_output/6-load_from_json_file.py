#!/usr/bin/python3
'''Im bored of this des..'''


import json


def load_from_json_file(filename):
    ''' is it that important u kiddin  '''
    with open(filename, "r", encoding="UTF-8") as file:
        j = file.read()
        o = json.loads(j)
        return(o)
