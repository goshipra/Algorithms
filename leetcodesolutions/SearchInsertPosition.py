#!/usr/bin/env python3
# SearchInsertPosition.py
# Author : Shipra


class Solution:
    """
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found. If not, return the index
    where it would be if inserted in order. Runs in O(log n) time.
    """

    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == "__main__":
    nums = [0, 1, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 22, 23, 24, 28, 30]
    target = 16
    print(Solution().searchInsert(nums, target))
