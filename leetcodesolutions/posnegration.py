#!/usr/bin/env python3
# posnegration.py
# Author : Shipra

def countratio(array):
    dict = {"pos":0,"neg":0,"zero":0}
    n = len(array)

    for element in array:
        if element > 0:
            dict["pos"] = dict["pos"] + 1
        elif element == 0:
            dict["neg"] = dict["neg"] + 1
        else:
            dict["zero"] = dict["zero"] + 1


    for element in dict:
        print(dict[element]/n)


array = [-4, 3, -9, 0, 4, 1]
countratio(array)