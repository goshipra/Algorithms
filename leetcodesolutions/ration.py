#!/usr/bin/env python3
# ration.py
# Author : Shipra


def count_ratio(array):
    """Print the frequency and relative frequency of each element."""
    counts = {}
    n = len(array)

    for element in array:
        counts[element] = counts.get(element, 0) + 1

    for element in counts:
        print(counts[element] / n)


if __name__ == "__main__":
    array = [-4, 3, -9, 0, 4, 1]
    count_ratio(array)
