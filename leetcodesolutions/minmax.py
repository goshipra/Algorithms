#!/usr/bin/env python3
# minmax.py
# Author : Shipra


def mini_max_sum(arr):
    """Print the smallest and largest sums obtainable from n-1 elements."""
    arr = sorted(arr)
    smallest_sum = sum(arr[:-1])
    largest_sum = sum(arr[1:])
    print(smallest_sum, largest_sum)


if __name__ == "__main__":
    array = [4, 3, 9, 0, 1]
    mini_max_sum(array)
