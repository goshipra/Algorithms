#!/usr/bin/env python3
# new.py
# Author : Shipra

# Read lines from a file and print only the odd-numbered lines.


def get_odd_lines(path):
    with open(path, "rt") as f:
        for i, line in enumerate(f):
            if i % 2 != 0:
                print(i, line)


def get_odd_lines_alternative(path):
    with open(path, "rt") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            if i % 2 != 0:
                print(lines[i])


if __name__ == "__main__":
    get_odd_lines("abc.txt")
    get_odd_lines_alternative("abc.txt")
