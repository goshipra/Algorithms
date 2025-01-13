#!/usr/bin/env python3
# bubbleSort.py
# Author : Shipra
import logging

def userInput():
    '''
    Taking numbers as user input and
    creating a  list of numbers
    '''
    initialListOfNumbers = []
    userInputNumber = 0
    while userInputNumber != '':
        userInputNumber = input("Enter the value to create a list and press enter: ")
        initialListOfNumbers.append(userInputNumber)


    initialListOfNumbers.pop()
    initialListOfNumbers = list(map(int, initialListOfNumbers))
    return initialListOfNumbers


def bubbleSortNumbers(initialListOfNumbers):
    '''
    Sorting a list of numbers using
    bubble sort algorithm
    '''
    for i in range(len(initialListOfNumbers) - 1):
        for j in range(len(initialListOfNumbers) - 1):
            if initialListOfNumbers[j] > initialListOfNumbers[j + 1]:
                initialListOfNumbers[j], initialListOfNumbers[j + 1] = \
                    initialListOfNumbers[j+1], initialListOfNumbers[j]
                logging.debug(initialListOfNumbers)
            else:
                continue

    print("The final sorted list:", initialListOfNumbers)

logging.basicConfig(level=logging.DEBUG)

for number in range(1):
    initialListOfNumbers = userInput()
    print("Original list of numbers" + str(number) + " =", initialListOfNumbers)
    logging.debug(initialListOfNumbers)
    bubbleSortNumbers(initialListOfNumbers)
