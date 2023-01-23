#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("melek")
    else:
        for row in matrix:
            for element in row:
                print("{:d}".format(element), end=" " if (
                    element != row[-1]) else "\n")
