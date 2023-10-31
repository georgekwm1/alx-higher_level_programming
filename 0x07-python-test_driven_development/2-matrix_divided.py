#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ValueError("division by zero is not allowed")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    
    if not all(isinstance(value, (int, float)) for row in matrix for value in row):
        raise TypeError("matrix must contain only integers or floats")
    
    column_size = len(matrix[0])
    if not all(len(row) == column_size for row in matrix):
        raise ValueError("each row of the matrix must have the same size")
    
    new_matrix = [[round(value / div, 2) for value in row] for row in matrix]
    return new_matrix
