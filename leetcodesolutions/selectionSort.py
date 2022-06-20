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


def SelectionSortNumbers(initialListOfNumbers):
    '''
    Sorting a list of numbers using
    selection sort algorithm
    '''
    newlist = []
    for i in range(len(initialListOfNumbers)):
        minimum = i
        for j in range(i+1,len(initialListOfNumbers)):
            if initialListOfNumbers[j] < initialListOfNumbers[minimum]:
                minimum = j
        logging.debug(initialListOfNumbers)
        initialListOfNumbers[i],initialListOfNumbers[minimum] =  initialListOfNumbers[minimum] , initialListOfNumbers[i]



    print("The final sorted list:", initialListOfNumbers)





logging.basicConfig(level=logging.DEBUG)

for number in range(1):
    initialListOfNumbers = userInput()
    print("Original list of numbers" + str(number) + " =", initialListOfNumbers)
    logging.debug(initialListOfNumbers)
    SelectionSortNumbers(initialListOfNumbers)
