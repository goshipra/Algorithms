#!/usr/bin/env python3
# ZigZag.py
# Author : Shipra

def ZigZag(Array,n):
    if len(Array) % 2 != 0:
        for i in range(1, len(Array), 2):
            if Array[i] < Array[i + 1]:
                if Array[i - 1] < Array[i + 1]:
                    Array[i], Array[i + 1] = Array[i + 1], Array[i]
                else:
                    Array[i - 1], Array[i] = Array[i], Array[i - 1]
            else:
                if Array[i] < Array[i - 1]:
                    Array[i], Array[i - 1] = Array[i - 1], Array[i]
    else:
        for i in range(1, len(Array) - 1, 2):
            print(Array[i])
            if Array[i] < Array[i + 1]:
                if Array[i - 1] < Array[i + 1]:
                    Array[i], Array[i + 1] = Array[i + 1], Array[i]
                else:
                    Array[i - 1], Array[i] = Array[i], Array[i - 1]
            else:
                if Array[i] < Array[i - 1]:
                    Array[i], Array[i - 1] = Array[i - 1], Array[i]
        if Array[i + 2] < Array[i + 1]:
            Array[i + 2], Array[i + 1] = Array[i + 1], Array[i + 2]

    return Array


InputArray = [4, 3, 7, 8, 6, 2, 1]
print(ZigZag(InputArray,len(InputArray)))
