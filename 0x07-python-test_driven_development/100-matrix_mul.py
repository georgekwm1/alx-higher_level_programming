#!/usr/bin/python3
"""
Definition of a fuction that multipies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.
    :param m_a: Matrix A as a list of lists.
    :type m_a: List[List[int]]
    :param m_b: Matrix B as a list of lists.
    :type m_b: List[List[int]]
    :return: The resultant matrix after multiplication.
    :rtype: List[List[int]]
    """
    # Check if the number of columns in first matrix is equal to the number of rows in second matrix
    
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list")

    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    

    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")
    
    if len(m_a) == 0 and len(m_b) == 0:
        raise ValueError("Input list of lists")
    
    if not all(isinstance(value, (int, float)) for row in m_a for value in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(value, (int, float)) for row in m_b for value in row):
        raise TypeError("m_b should contain only integers or floats")
    
    for rows in m_a:
        if not len(rows) == len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for rows in m_b:
        if not len(rows) == len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        
    result = [[0]*len(m_b[0]) for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result