#!/usr/bin/env python3
# Duplicates.py
# Author : Shipra

class Solution(object):
    def containsDuplicate(self, nums):
        '''
        Given an integer array nums, return true if any
        value appears at least twice in the array,
         and return false if every element is distinct.
        '''
        newlist = set()
        for num in nums:
            if num in newlist:
                return True
            else:
                newlist.add(num)

        return False


nums = [1,2,3,1]
obj = Solution()
print(obj.containsDuplicate(nums))
