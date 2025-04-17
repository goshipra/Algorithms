#!/usr/bin/env python3
# Equality.py
# Author : Shipra

Array1 = [1, 2, 3, 6, 5, 7,8]
Array2 = [7, 5, 4, 3, 2, 1]

flag = True
if len(Array2) == len(Array1):
    for element in Array1:
        if element not in Array2:
            flag = False
            break
        else:
            flag = True
            continue
else:
    flag = False        

print(flag)
