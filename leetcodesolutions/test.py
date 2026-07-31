#!/usr/bin/env python3
# test.py
# Author : Shipra


def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    return result + list1[i:] + list2[j:]


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [4, 5, 6, 7, 8, 8, 9]
    print(merge_sorted_lists(list1, list2))
