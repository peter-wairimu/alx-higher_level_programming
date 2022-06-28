#!/usr/bin/python3
"""
A class that avoids dynmaically created attributes
"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
