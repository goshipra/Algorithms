#!/usr/bin/env python3
# secondLargest.py
# Author : Shipra

Array = [5, 4, 7, 8, 2, 3, 9, 10, 11, 99]

if Array[0] > Array[1]:
    largest = Array[0]
    secondLargest = Array[1]
else:
    largest = Array[1]
    secondLargest = Array[0]

for i in range(2, len(Array)):
    if Array[i] > largest:
        temp = largest
        largest = Array[i]
        secondLargest = temp
    else:
        if Array[i] > secondLargest:
            secondLargest = Array[i]
        else:
            continue
print("Second largest element :", secondLargest)
