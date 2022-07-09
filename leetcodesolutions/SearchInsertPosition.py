#!/usr/bin/env python3
# SearchInsertPosition.py
# Author : Shipra

class Solution(object):
    def searchInsert(self, nums, target):
        """
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the index
         where it would be if it were inserted in order.
        You must write an algorithm with O(log n) runtime complexity.
        """
        if len(nums) < 1:
            return 0
        i=0
        if target in nums:
            return nums.index(target)

        else:
            mid = (len(nums) /2)

            if nums[mid] < target:
                while mid <= len(nums)-1:
                    if nums[mid] < target < nums[mid + 1]:
                        return mid + 1
            elif nums[mid] > target:
                while mid >= target:
                    if nums[i] < target < nums[mid]:
                        return





nums = [1,3,5,6]
target = 7
obj = Solution()
print(obj.searchInsert(nums,target))


