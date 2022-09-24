#!/usr/bin/env python3
# insertionSort.py
# Author : Shipra

InputList = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
counter = 0
for i in range(1, len(InputList)):
    j = i - 1
    temp = InputList[i]
    while j >= 0 and InputList[j] >= temp:
        InputList[j + 1] = InputList[j]
        counter += 1
        j -= 1
    InputList[j + 1] = temp
print(InputList)
print(counter)
