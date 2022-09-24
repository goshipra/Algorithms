#!/usr/bin/env python3
# fibbonacci.py
# Author : Shipra
#
# def fibbonacci(n):
#     if n <= 1:
#         return n
#     i = 1
#     fiblist = [0, 1]
#     while i < n:
#         fiblist.append(fiblist[len(fiblist)-1] + fiblist[len(fiblist)-2])
#         i += 1
#     return fiblist
#

def fibbonacci(n):
    if n <= 1:
        return n

    return fibbonacci(n - 1) + fibbonacci(n - 2)


for i in range(0, 8):
    print(fibbonacci(i))
