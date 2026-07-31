#!/usr/bin/env python3
# RemoveElement.py
# Author : Shipra


class Solution:
    """
    Given an integer array nums and an integer val, remove all
    occurrences of val in nums in-place; order may change. Return k,
    the number of remaining elements, with the first k slots of nums
    holding the result.
    """

    def removeElement(self, nums, val):
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(Solution().removeElement(nums, val))
