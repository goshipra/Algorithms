#!/usr/bin/env python3
# degreearray.py
# Author : Shipra


class Solution:
    """
    Given a non-empty array of non-negative integers nums, the degree is
    the maximum frequency of any element. Return the length of the
    shortest contiguous subarray with the same degree as nums.
    """

    def findShortestSubArray(self, nums):
        frequency = {}
        first_index = {}
        last_index = {}

        for i, num in enumerate(nums):
            frequency[num] = frequency.get(num, 0) + 1
            first_index.setdefault(num, i)
            last_index[num] = i

        degree = max(frequency.values())
        return min(
            last_index[num] - first_index[num] + 1
            for num in frequency
            if frequency[num] == degree
        )


if __name__ == "__main__":
    nums = [1, 2, 2, 2, 3, 1, 1, 1]
    print(Solution().findShortestSubArray(nums))
