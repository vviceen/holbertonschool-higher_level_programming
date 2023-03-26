#!/usr/bin/python3
""" task 5"""


def text_indentation(text):
    """" prints a text with 2 new lines after ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indent = [".", "?", ":"]
    for idx, letter in enumerate(text):
        if idx > 0 and text[idx - 1] in indent and letter == " ":
            continue
        print(letter, end="")
        if letter in indent:
            print("\n\n", end="")
