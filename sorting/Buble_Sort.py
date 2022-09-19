#!/usr/bin/env python3
# Buble_Sort.py
# Author : Shipra


def BubbleSort(lista):
    """
    Optimized Bubble sort
    : If list is already sorted it will break in one pass
    """

    outerloop = 0
    while outerloop < len(lista) - 1:
        itr = 0
        checker = 0
        while itr < len(lista) - 1:
            if lista[itr] > lista[itr + 1]:
                lista[itr], lista[itr + 1] = lista[itr + 1], lista[itr]
                checker += 1
            itr += 1

        print("array: ", lista)

        if checker == 0:
            break
        outerloop += 1
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 7, 88]
sortedlist = BubbleSort(lista)
print("final array: ", sortedlist)
