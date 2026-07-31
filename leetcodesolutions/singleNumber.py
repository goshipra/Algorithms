#!/usr/bin/env python3
# singleNumber.py
# Author : Shipra


class Solution:
    """
    Given a non-empty array of integers nums, every element appears
    twice except for one. Find that single one, in linear time and
    constant extra space.
    """

    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    arr = [2, 2, 1]
    print(Solution().singleNumber(arr))
