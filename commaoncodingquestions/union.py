#!/usr/bin/env python3
# union.py
# Author : Shipra

def union(Array1, Array2):
    for element in Array2:
        if element in Array1:
            continue
        else:
            Array1.append(element)
    return Array1


Array1 = [1, 2, 3, 7, 8]
Array2 = [1, 2, 3, 4, 5]
print(union(Array1,Array2))
