#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    if x == 0:
        print()
        return i
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            print()
            return(i)
    print()
    return(i + 1)
