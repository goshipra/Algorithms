#!/usr/bin/env python3
# selectionSort.py
# Author : Shipra

import logging


def user_input():
    """Take numbers as user input and build a list of ints."""
    numbers = []
    value = None
    while value != "":
        value = input("Enter the value to create a list: ")
        if value != "":
            numbers.append(int(value))
    return numbers


def selection_sort(numbers):
    """Sort a list of numbers using the selection sort algorithm."""
    for i in range(len(numbers)):
        minimum = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[minimum]:
                minimum = j
        numbers[i], numbers[minimum] = numbers[minimum], numbers[i]
        logging.debug(numbers)
    return numbers


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    initial_numbers = user_input()
    print("Original list of numbers =", initial_numbers)
    print("The final sorted list:", selection_sort(initial_numbers))
