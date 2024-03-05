#!/usr/bin/python3
"""Define a class Square"""
class Square:
    def __init__(self, size=0):
        self._size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self._size ** 2
