#!usr/bin/python3
"""
Module that contains function that reads from a file.
"""


def read_file(filename = ""):
    """
    Function that reads from a file.
    Args:
        filename: name of the file to read
    Raises:
        IOError: if the file can't be opened
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
