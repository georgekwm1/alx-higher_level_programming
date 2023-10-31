#!/usr/bin/python3
"""Definition of function that Divides a matrix by a divisor"""

def matrix_divided(matrix, div):
    """
    This function Divides a matrix by a divisor.

    Args:
    matrix (int, float): First integer.
    div (int, float): Second integer.

    Returns:
    int o float: a new matrix.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ValueError("division by zero is not allowed")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(value, (int, float)) for row in matrix for value in row):
        raise TypeError("matrix must contain only integers or floats")
    
    column_size = len(matrix[0])
    if not all(len(row) == column_size for row in matrix):
        raise ValueError("Each row of the matrix must have the same size")
    
    new_matrix = [[round(value / div, 2) for value in row] for row in matrix]
    return new_matrix
