#!/usr/bin/python3
for value in range(0, 100):
    print("{:02}".format(value), end=", ")
    if value == 99:
        print("{:02}".format(value))
