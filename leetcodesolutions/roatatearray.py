#!/usr/bin/env python3
# roatatearray.py
# Author : Shipra


class Solution:
    """
    Given an array nums, rotate it to the right by k steps in-place,
    where k is non-negative.
    """

    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


if __name__ == "__main__":
    nums = [-1, -100, 3, 99]
    k = 2
    Solution().rotate(nums, k)
    print(nums)
