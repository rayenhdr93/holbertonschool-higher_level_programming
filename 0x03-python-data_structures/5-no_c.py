#!/usr/bin/python3
def no_c(my_string):
    x = len(my_string)
    i = 0
    while i < x:
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            my_string = my_string[:i] + my_string[i+1:]
            x = x - 1
        else:
            i += 1
    return(my_string)
