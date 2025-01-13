#!/usr/bin/env python3
# insertionsort.py
# Author : Shipra
import logging
import sys


def userInput():
    '''
    Taking numbers as user input and
    creating a  list of numbers
    '''
    initialListOfNumbers = []
    userInputNumber = 0
    while userInputNumber != '':
        userInputNumber = input("Enter the value to create a list: ")
        initialListOfNumbers.append(userInputNumber)

    initialListOfNumbers.pop()
    initialListOfNumbers = list(map(int, initialListOfNumbers))
    return initialListOfNumbers


def InsertionSortNumbers(iLON):
    '''
    Sorting a list of numbers using
    insertion sort algorithm
    '''
    for i in range(1,len(iLON)):
        key = iLON[i]
        j = i -1
        while j >= 0 and iLON[j] > key:
            iLON[j+1] = iLON[j]
            j -= 1
        iLON[j+1] = key

    print(iLON)


logging.basicConfig(level=logging.DEBUG)

for number in range(1):
    initialListOfNumbers = userInput()
    print("Original list of numbers" + str(number) + " =", initialListOfNumbers)
    logging.debug(initialListOfNumbers)
    InsertionSortNumbers(initialListOfNumbers)
