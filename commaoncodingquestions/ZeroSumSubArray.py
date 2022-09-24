#!/usr/bin/env python3
# ZeroSumSubArray.py
# Author : Shipra

def findSubArray(Array):
    """
    You are given an array arr[] of size n.
     Find the total count of sub-arrays having
     their sum equal to 0.
    """
    subArray = []
    for i in range(0, len(Array)):
        if Array[i] == 0:
            subArray.append([Array[i]])
        Sum = Array[i]
        newSubArray = [Array[i]]
        for j in range(i + 1, len(Array)):
            print(i, j)
            Sum += Array[j]
            newSubArray.append(Array[j])
            print("Sum: ", Sum)
            print("newSubArray:", newSubArray)
            if Sum == 0:
                print("Got it")
                subArray.append(newSubArray)
                break
            else:
                continue

    return subArray


Array = [6, -1, -3, 4, -2, 2, 4, 6, -12, -7]
print(findSubArray(Array))
