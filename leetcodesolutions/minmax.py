#!/usr/bin/env python3
# minmax.py
# Author : Shipra


def miniMaxSum(arr):
    arr.sort()
    print(arr)
    lenght = len(arr)
    min,max =0,0

    for i in range(0,lenght-1):
        min = min + arr[i]

    for i in range(1,lenght):
        max = max + arr[i]

    print(min,max)


array = [4, 3, 9, 0, 1]
miniMaxSum(array)