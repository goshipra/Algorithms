#!/usr/bin/env python3
# Linear.py
# Author : Shipra

def LinearSearch(list, target):
    position = []
    NotFound = "NotFound"
    for i in range(len(list)):
        if list[i] == target:
            position.append(i)
    if len(position) == 0:
        return NotFound
    else:
        return position


InputArray = [22, 6, 29, 44, 20, 13, 56, 32, 21, 67, 32]
Target = 32
print(LinearSearch(InputArray, Target))
