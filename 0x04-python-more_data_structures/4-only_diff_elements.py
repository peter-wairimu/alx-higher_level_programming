#!/usr/bin/python3
def only_diff_elements(set_1=[], set_2=[]):
    if set_1 is None or len(set_1) == 0:
        return set_1
    if set_2 is None or len(set_2) == 0:
        return set_2

    return set_1 ^ set_2
