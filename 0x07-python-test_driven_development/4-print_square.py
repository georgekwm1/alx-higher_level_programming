#!/usr/bin/python3
def print_square(size):
    symbol = "#"
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not size:
        raise ValueError("Input an Integer")
    for i in range(size):
        print("{}".format(symbol * size), end='\n')
