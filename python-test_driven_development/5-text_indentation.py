#!/usr/bin/python3
""" task 5"""


def text_indentation(text):
    """" prints a text with 2 new lines after ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    indent = [".", "?", ":"]
    no_space = False
    for idx, letter in enumerate(text):
        if no_space:
            if letter == " ":
                continue
        no_space = False
        if idx > 0 and text[idx - 1] in indent and letter == " ":
            no_space = True
            continue
        print(letter, end="")
        if letter in indent:
            print("\n\n", end="")
