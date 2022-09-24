#!/usr/bin/env python3
# factorial.py
# Author : Shipra


def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n-1)


print(factorial(7))
for i in range(1, 8):
    print(factorial(i))

