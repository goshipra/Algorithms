#!/usr/bin/env python3
# selectionSort.py
# Author : Shipra

InputList = [10, 9, 8, 7, 6, 5, 4, 3]

for i in range(0, len(InputList) - 1):
    minimum = i
    for j in range(i + 1, len(InputList)):
        if InputList[minimum] > InputList[j]:
            minimum = j
        else:
            continue
    print("minimum: ", InputList[minimum])
    InputList[i], InputList[minimum] = InputList[minimum], InputList[i]
    print(InputList)

print(InputList)
