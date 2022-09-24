#!/usr/bin/env python3
# quickSort.py
# Author : Shipra


def Partition(InputList, lb, ub):
    pivot = InputList[lb]
    start = lb + 1
    end = ub

    while start < end:
        while InputList[start] <= pivot:
            start += 1
        while InputList[end] > pivot:
            end -= 1

        if start < end:
            InputList[start], InputList[end] = InputList[end], InputList[start]
        else:
            break
        print(InputList)

    InputList[lb], InputList[end] = InputList[end], InputList[lb]
    print(InputList)

    return end


def QuickSort(InputList, lb, ub):
    if len(InputList) <= 1:
        return InputList
    print(lb,ub)
    if lb < ub:
        pivotLoc = Partition(InputList, lb, ub)
        QuickSort(InputList, lb, pivotLoc - 1)
        QuickSort(InputList, pivotLoc + 1, ub)


InputList = [1,2,3,4,5,6,7,8]

QuickSort(InputList, 0, len(InputList)-1)
print(InputList)
