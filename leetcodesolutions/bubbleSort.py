#!/usr/bin/env python3
# bubbleSort.py
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


def bubble_sort(numbers):
    """Sort a list of numbers using the bubble sort algorithm."""
    for i in range(len(numbers) - 1):
        swapped = False
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        logging.debug(numbers)
        if not swapped:
            break
    return numbers


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    initial_numbers = user_input()
    print("Original list of numbers =", initial_numbers)
    print("The final sorted list:", bubble_sort(initial_numbers))
