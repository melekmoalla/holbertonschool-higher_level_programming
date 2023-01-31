#!/usr/bin/python3
"""
    Function that divided element in the matrix bu=y div 2.
    matrix and div must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
    matrix and div must be first casted to integers if they are float
    Returns an integer: matrix modify
"""


def matrix_divided(matrix, div):
    """
    Function that divided element in the matrix bu=y div 2.
    matrix and div must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer or b must be an integer
    matrix and div must be first casted to integers if they are float
    Returns an integer: matrix modify
    """
    a = 0
    m = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    i = 0
    b = len(matrix[i])
    v = "matrix must be a matrix (list of lists) of integers/floats"
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
                    v)
            m[i][a] = round((matrix[i][a]/div), 2)
    return (m)
