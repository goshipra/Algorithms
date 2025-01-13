#!/usr/bin/env python3
# MajorityElements.py
# Author : Shipra

class Solution(object):
    def majorityElement(self, nums):
        '''
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋
         times. You may assume that the majority element always exists
          in the array.
           '''
        newDict = {}
        convertedSet = set(nums)
        for element in convertedSet:
            countOfValue = nums.count(element)
            newDict[countOfValue] = element

        maxValue = max(newDict)
        print(maxValue)
        return newDict[maxValue]


nums = [2,2,1,1,1,1,2,2,2,2]
obj = Solution()
print(obj.majorityElement(nums))
