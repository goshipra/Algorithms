#!/usr/bin/env python3
# merge_sort.py
# Author : Shipra


def user_input():
    """Take numbers as user input and build a list of ints."""
    numbers = []
    value = None
    while value != "":
        value = input("Enter the value to create a list: ")
        if value != "":
            numbers.append(int(value))
    return numbers


def merge_sort(numbers):
    """Sort a list of numbers in place using the merge sort algorithm."""
    if len(numbers) <= 1:
        return numbers

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        numbers[k] = right[j]
        j += 1
        k += 1

    return numbers


if __name__ == "__main__":
    initial_numbers = user_input()
    print("Original list of numbers =", initial_numbers)
    print(merge_sort(initial_numbers))
