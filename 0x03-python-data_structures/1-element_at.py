#!/usr/bin/python3
def element_at(my_list, idx):
    if (not(idx in range(0, len(my_list)))):
        return(None)
    elif (my_list[idx] < 0):
        return(None)
    else:
        return(my_list[idx])
