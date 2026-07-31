#!/usr/bin/env python3
# MajorityElements.py
# Author : Shipra

from collections import Counter


class Solution:
    """
    Given an array nums of size n, return the majority element. The
    majority element is the element that appears more than n // 2 times.
    Assumes the majority element always exists in the array.
    """

    def majorityElement(self, nums):
        counts = Counter(nums)
        return counts.most_common(1)[0][0]


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 1, 2, 2, 2, 2]
    print(Solution().majorityElement(nums))
