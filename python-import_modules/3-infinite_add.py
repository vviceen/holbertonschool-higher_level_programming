#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    for n in range(1, len(argv)):
        total += int(argv[n])
    print(total)
