#!/usr/bin/python3
""" task 1 """


def write_file(filename="", text=""):
    """ write a string to a text file 
    and returns the number of characters written """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
