#!/usr/bin/python3
""" task 0 """


def read_file(filename=""):
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content)
