#!/usr/bin/env python3
# mostfrequent.py
# Author : Shipra

from collections import Counter


class Solution:
    """
    Given an integer array nums, return the most frequent even element.
    If there is a tie, return the smallest one. If no even element
    exists, return -1.
    """

    def mostFrequentEven(self, nums):
        counts = Counter(num for num in nums if num % 2 == 0)
        if not counts:
            return -1

        maximum = max(counts.values())
        return min(num for num, count in counts.items() if count == maximum)


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 4, 4, 1]
    print(Solution().mostFrequentEven(nums))
