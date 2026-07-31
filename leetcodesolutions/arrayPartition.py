#!/usr/bin/env python3
# arrayPartition.py
# Author : Shipra


class Solution:
    """
    Given an integer array nums of 2n integers, group these integers into
    n pairs so that the sum of the minimum of each pair is maximized.
    """

    def arrayPairSum(self, nums):
        nums.sort()
        return sum(nums[::2])


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    print(Solution().arrayPairSum(nums))
