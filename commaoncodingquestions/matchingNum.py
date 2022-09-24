#!/usr/bin/env python3
# matchingNum.py
# Author : Shipra

def matchingNumbers(Array):
    Newset = set()
    for element in Array:
        if element in Newset:
            print(element)
        else:
            Newset.add(element)


Array = [1, 4, 5, 6, 5, 8, 6]
matchingNumbers(Array)
