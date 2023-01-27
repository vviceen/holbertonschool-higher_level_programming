#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    maxval = 0
    for idx in range(0, len(my_list) - 1):
        if my_list[idx] > maxval:
            maxval = my_list[idx]
    return maxval
