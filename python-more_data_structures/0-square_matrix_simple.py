#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matr = [[0 for i in range(3)] for j in range(3)]
    for i in range(len(matrix)):
        for m in range(len(matr[i])):
            matr[i][m] = matrix[i][m]*matrix[i][m]
    return (matr)
