#!/usr/bin/python3
"""Define a class Square"""
class Square:
    def __init__(self, size=0):
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._size = value

    def area(self):
        return self._size ** 2

