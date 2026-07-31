#!/usr/bin/env python3
# binarySearch.py
# Author : Shipra


class Solution:
    """
    Standard binary search over a sorted array.
    """

    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1


if __name__ == "__main__":
    nums = [20, 30, 90, 90, 90, 90, 95, 97, 98, 99, 100]
    target = 90
    print(Solution().search(nums, target))
