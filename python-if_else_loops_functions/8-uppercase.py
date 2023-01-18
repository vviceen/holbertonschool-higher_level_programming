#!/bin/usr/python3
def uppercase(str):
    for word in str:
        if ord(word) >= 97 and ord(word) <= 122:
            print("{:c}".format(ord(word) - 32))
        else:
            print(word)
