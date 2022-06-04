#!/usr/bin/env python3
# insertionsort.py
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
        userInputNumber = input("Enter the value to create a list: ")
        initialListOfNumbers.append(userInputNumber)

    initialListOfNumbers.pop()
    initialListOfNumbers = list(map(int, initialListOfNumbers))
    return initialListOfNumbers


def MergeSortNumbers(initialListOfNumbers,k):
    '''
    Sorting a list of numbers using
    MergeSortNumbers sort algorithm
    '''
    logging.debug(initialListOfNumbers)
    if len(initialListOfNumbers) <=1 :
        print(" List is already sorted ")

    if len(initialListOfNumbers) > 1:
        midvalue = len(initialListOfNumbers)//2
        leftlist = initialListOfNumbers[:midvalue]
        rightlist = initialListOfNumbers[midvalue:]
        print(leftlist)
        print(rightlist)
        print("pass: ", k)
        k+=1
        MergeSortNumbers(leftlist,k)
        MergeSortNumbers(rightlist,k)

        i = j = l = 0

        while len(leftlist) > i and len(rightlist) > j:
            if leftlist[i] > rightlist[j]:
                initialListOfNumbers[l] = rightlist[j]
                j+=1
            else:
                initialListOfNumbers[l] = leftlist[i]
                i+=1
            l+=1


        while i < len(leftlist):
            initialListOfNumbers[l] = leftlist[i]
            i += 1
            l += 1

        while j < len(rightlist):
            initialListOfNumbers[l] = rightlist[j]
            j += 1
            l += 1

    print(initialListOfNumbers)



logging.basicConfig(level=logging.DEBUG)

for number in range(1):
    initialListOfNumbers = userInput()
    print("Original list of numbers" + str(number) + " =", initialListOfNumbers)
    logging.debug(initialListOfNumbers)
    k=1
    MergeSortNumbers(initialListOfNumbers,k)
