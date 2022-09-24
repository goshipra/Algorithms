#!/usr/bin/env python3
# .py
# Author : Shipra

def BinarySearch(InputArray, target):
    leftptr = 0
    rigthptr = len(InputArray) - 1

    while leftptr <= rigthptr:
        midptr = (leftptr + rigthptr) // 2
        if InputArray[midptr] == target:
            return midptr
        elif InputArray[midptr] < target:
            leftptr = midptr + 1

        elif InputArray[midptr] > target:
            rigthptr = midptr - 1

    return "Not Found"


InputArray = [5, 7, 8, 9, 16, 32, 43, 56, 76, 89, 90]
Target = 76
print("Location found at:  ", BinarySearch(InputArray, Target))
