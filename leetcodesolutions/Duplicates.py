#!/usr/bin/env python3
# Duplicates.py
# Author : Shipra


class Solution:
    """
    Given an integer array nums, return true if any value appears at
    least twice in the array, and false if every element is distinct.
    """

    def containsDuplicate(self, nums):
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().containsDuplicate(nums))
