#!/usr/bin/env python3
# firstLastPosition.py
# Author : Shipra


class Solution:
    """
    Given an array of integers nums sorted in increasing order, find the
    starting and ending position of a given target value. If target is
    not found in the array, return [-1, -1]. Runs in O(log n) time.
    """

    def searchRange(self, nums, target):
        first = self._binary_search(nums, target, leftmost=True)
        if first == -1:
            return [-1, -1]
        last = self._binary_search(nums, target, leftmost=False)
        return [first, last]

    def _binary_search(self, nums, target, leftmost):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                if leftmost:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result


if __name__ == "__main__":
    nums = [1, 2, 3, 3, 3, 3, 3, 3, 5, 6]
    target = 3
    print(Solution().searchRange(nums, target))
