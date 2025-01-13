#!/usr/bin/env python3
# ratio.py
# Author : Shipra

def countratio(array):
    dict = {}
    n = len(array)

    for element in array:
        if element in dict:
            dict[element] = dict[element] + 1
        else:
            dict[element] = 1
    print(dict)

    for element in dict:
        print(dict[element]/n)


array = [-4, 3, -9, 0, 4, 1]
countratio(array)