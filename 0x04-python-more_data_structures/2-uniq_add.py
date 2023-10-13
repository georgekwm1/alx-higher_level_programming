#!/usr/bin/python3
def uniq_add(my_list=[]):
    addition = 0
    unique = set(my_list)
    for numbers in unique:
        addition += numbers
    return addition
