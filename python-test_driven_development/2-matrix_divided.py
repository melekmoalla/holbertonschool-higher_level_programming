#!/usr/bin/python3

def matrix_divided(matrix, div):
    a = 0
    m = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    i = 0
    b = len(matrix[i])
    if type(div) not in [int, float]:
        raise TypeError(
            "div must be a number")
    if (div == 0):
        raise ZeroDivisionError(
            "division by zero")
    for i in range(len(matrix)):
        if (b != len(matrix[i])):
            raise TypeError(
                "Each row of the matrix must have the same size")
        b = len(matrix[i])
        for a in range(len(matrix[i])):
            if type(matrix[i][a]) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            m[i][a] = round((matrix[i][a]/div), 2)
    return (m)
