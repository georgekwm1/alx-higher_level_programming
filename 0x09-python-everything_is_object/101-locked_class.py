#!/usr/bin/python3
class LockedClass:
    __slots__ = ('first_name',)  # Define allowed attribute(s) here
    
    def __init__(self, first_name):
        self.first_name = first_name
