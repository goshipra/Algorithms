#!/usr/bin/env python3
# reverseArray.py
# Author : Shipra

import math

def reverseArray(Array):
    j = len(Array) - 1

    for i in range(math.ceil(j / 2)):
        print(i,j)
        Array[i], Array[j] = Array[j], Array[i]
        j -= 1
    return Array


Array = [1, 2, 3, 45, 95, 78]
print(reverseArray(Array))

# midpoint = len(Array) // 2

# print(len(Array),midpoint)
# for i in range(midpoint):
#     for j in range (-1,midpoint,-1):
#         Array[i],Array[j] = Array[j], Array[i]
# print(Array)    
