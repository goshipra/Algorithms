#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# sequence.py
# Author : Shipra


def sequence(n):
    """Print the Collatz sequence starting from n down to 1."""
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1


if __name__ == "__main__":
    sequence(16)
