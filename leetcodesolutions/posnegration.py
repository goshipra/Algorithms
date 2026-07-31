#!/usr/bin/env python3
# posnegration.py
# Author : Shipra


def count_ratio(array):
    """Print the fraction of positive, negative, and zero elements."""
    counts = {"pos": 0, "neg": 0, "zero": 0}
    n = len(array)

    for element in array:
        if element > 0:
            counts["pos"] += 1
        elif element == 0:
            counts["zero"] += 1
        else:
            counts["neg"] += 1

    for key in counts:
        print(counts[key] / n)


if __name__ == "__main__":
    array = [-4, 3, -9, 0, 4, 1]
    count_ratio(array)
