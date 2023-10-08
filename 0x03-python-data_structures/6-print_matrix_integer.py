#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        row_string = ""
        for values in lists:
            row_string += str(values) + " "
        print(row_string.strip())
