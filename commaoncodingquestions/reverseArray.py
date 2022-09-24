#!/usr/bin/env python3
# reverseArray.py
# Author : Shipra

import math

def reverseArray(Array):
    j = len(Array) - 1

    for i in range(math.ceil(j / 2)):
        Array[i], Array[j] = Array[j], Array[i]
        j -= 1
    return Array


Array = [1, 2, 3, 45, 6]
print(reverseArray(Array))
