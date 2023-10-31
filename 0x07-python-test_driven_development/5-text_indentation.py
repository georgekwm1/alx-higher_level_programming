#!/usr/bin/python3

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end='')
        if char in (".", "?", ":"):
            print("\n\n", end='')
