#!/usr/bin/env python3
# RemoveDuplicates.py
# Author : Shipra


class Solution:
    """
    Given an integer array nums sorted in non-decreasing order, remove
    the duplicates in-place such that each unique element appears only
    once, keeping relative order. Return k, the number of unique
    elements, with the first k slots of nums holding the result.
    """

    def removeDuplicates(self, nums):
        if not nums:
            return 0

        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))
