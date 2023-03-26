#!/usr/bin/python3
""" task 4"""


def print_square(size):
    """ prints a square with the character #. """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
