#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (not(idx in range(0, len(my_list)))):
        return(my_list)
    elif (my_list[idx] < 0):
        return(my_list)
    else:
        my_list[idx] = element
        return(my_list)
