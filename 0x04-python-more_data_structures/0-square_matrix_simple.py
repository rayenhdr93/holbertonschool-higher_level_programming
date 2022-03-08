#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Sqmatrix = [[None for x in range(len(matrix[0]))] for y in range(
        len(matrix))]
    x = 0
    for ar in matrix:
        y = 0
        for i in ar:
            Sqmatrix[x][y] = i ** 2
            y += 1
        x += 1
    return Sqmatrix
