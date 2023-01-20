#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments".format(len(argv) - 1), end="")
        if len(argv) == 1:
            print(".")
        else:
            print(":")
            for n in range(1, len(argv)):
                print("{}: {}".format(n, argv[n]))
