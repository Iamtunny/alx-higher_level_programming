#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for j in range(len(matrix)):
        for i in range(len(matrix[i])):
            print("{:d}".format(matrix[j][i]), end="")
            if i != len(matrix[j]) - 1:
                print(" ", end="")
        print("")
