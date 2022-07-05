#!usr/bin/python3
"""
Module that contains a function that retuns the number of lines in a file
"""


def write_file(filename="", text=""):
    """ Function that writes to a file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """

    with open(filename, mode='w+') as f:
        return f.write(text)
