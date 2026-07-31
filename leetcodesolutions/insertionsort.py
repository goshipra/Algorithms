#!/usr/bin/env python3
# insertionsort.py
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


def insertion_sort(numbers):
    """Sort a list of numbers using the insertion sort algorithm."""
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    initial_numbers = user_input()
    print("Original list of numbers =", initial_numbers)
    logging.debug(initial_numbers)
    print(insertion_sort(initial_numbers))
