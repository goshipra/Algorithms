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

        if target in nums:
            return nums.index(target)

        else:
            start = 0
            end = len(nums) - 1

            if nums[end] < target:
                return end + 1

            if nums[start] > target:
                return start

            while start <= end:
                mid = start + (end - start)//2
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start




nums = [0,1,3,5,6,8,9,10,11,12,13,14,15,17,18,19,20,22,23,24,28,30]
target = 16
obj = Solution()
print(obj.searchInsert(nums,target))


