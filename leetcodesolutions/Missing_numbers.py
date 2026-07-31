#!/usr/bin/env python3
# Missing_numbers.py
# Author : Shipra


class Solution:
    """
    Given an array nums containing n distinct numbers in the range
    [0, n], return the one number missing from the range.
    """

    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        return expected_sum - sum(nums)


if __name__ == "__main__":
    arr = [0, 2, 3]
    print(Solution().missingNumber(arr))
