#!/usr/bin/env python3
# AllElementSum.py
# Author : Shipra

Array = [1, 2, 3, 4, 5, 6, 78, 8]

sumofArray = 0
for i in range(len(Array)):
    sumofArray = sumofArray + Array[i]
print(sumofArray)

def allelements_sum(list1):
    summation = 0
    for element in list1:
        summation = element + summation
    print(summation)    

allelements_sum(Array)
