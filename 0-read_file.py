#!/usr/bin/python3
"""Defining a text file-reading function"""

def read_file(filename=""):
    """Print the content of a UTF-8 to the standard output"""
    with open(filename, encoding = "UTF-8") as f:
    print(f.read(), end = "")
