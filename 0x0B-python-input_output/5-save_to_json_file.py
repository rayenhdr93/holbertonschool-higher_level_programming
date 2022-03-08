#!/usr/bin/python3
'''Im bored of this des..'''


import json


def save_to_json_file(my_obj, filename):
    ''' is it that important u kiddin  '''
    j = json.dumps(my_obj)
    with open(filename, "a", encoding="UTF-8") as file:
        file.write(j)
