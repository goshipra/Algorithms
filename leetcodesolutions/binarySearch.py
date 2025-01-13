#!/usr/bin/env python3
# binarySearch.py
# Author : Shipra

class Solution:
    def search(self, nums, target):
        '''
        Binary search tree
        '''
        if not nums:
            return -1

        low = 0
        high = len(nums) - 1
        mid = int((high + low)/ 2)

        if target == nums[mid]:
            return mid

        while low <= high:
            mid = int((low + high) / 2)
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            elif target == nums[mid]:
                return mid

        return -1


nums = [20,30,90,90,90,90,95,97,98,99,100]
target = 90
obj = Solution()
print(obj.search(nums, target))
