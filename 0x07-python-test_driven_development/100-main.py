#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
print(matrix_mul([[1, 2], [3, 4], [5, 6]], [[5, 6, 7], [7, 8, 9]]))
try:
    print(matrix_mul([[1, 2], [3, 4]], [[1, "2"]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul())
except Exception as e:
    print(e)

try:
    print(matrix_mul([[1, 2], [3]], [[1, 2]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul("Holberton", [[5, 6], [7, 8]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[5, 6], [7, 8]], "Holberton"))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[]], [[5, 6], [7, 8]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[5, 6], [7, 8]], [[]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[5, "6"], [7, 8]], [[5, 6], [7, 8]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[5, 6], [7, 8]], [[5, "6"], [7, 8]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[5, 6, 10], [7, 8]], [[5, 6], [7, 8]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[5, 6], [7, 8]], [[5, 6, 1], [7, 8]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[1, 2, 3], [3, 4, 5]], [[1, 2], [3, 4]]))
except Exception as e:
    print(e)

