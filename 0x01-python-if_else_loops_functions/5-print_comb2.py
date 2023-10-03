#!/usr/bin/python3
for value in range(0, 100):
    print(f"{value:02}", end=", ")
    if value == 99:
        print(f"{value:02}")
