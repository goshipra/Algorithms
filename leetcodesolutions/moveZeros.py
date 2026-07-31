#!/usr/bin/env python3
# moveZeros.py
# Author : Shipra

# Given an integer array nums, move all 0's to the end of it while
# maintaining the relative order of the non-zero elements. Must be done
# in place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums):
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1

        for i in range(insert_pos, len(nums)):
            nums[i] = 0

        return nums


if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(arr))
