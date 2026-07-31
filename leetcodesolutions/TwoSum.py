#!/usr/bin/env python3
# TwoSum.py
# Author : Shipra


class Solution:
    """
    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target. Each input has
    exactly one solution, and the same element may not be used twice.
    """

    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))
