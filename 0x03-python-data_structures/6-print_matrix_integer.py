#!/usr/bin/python3
def print_matrix_integer(C=[[]]):
    for i in range(0, len(C)):
        for j in range(0, len(C[0])):
            if (j == len(C[0]) - 1):
                print("{:d}".format(C[i][j]), end="")
            else:
                print("{:d}".format(C[i][j]), end=" ")
        print()
