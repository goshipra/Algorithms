#!/usr/bin/env python3
# TwoSum.py
# Author : Shipra

class Solution(object):
    '''
    Given an array of integers nums and an integer target,
     return indices of the two numbers such that they add
     up to target.You may assume that each input would have
      exactly one solution, and you may not use the same
      element twice. You can return the answer in any order.
    '''

    def twoSum(self, nums, target):
        dictionary = {}

        for i in range(len(nums)):
            print("i: ",i)
            secondNumber = target-nums[i]
            print(dictionary)
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
            dictionary.update({nums[i]: i})

nums = [3,2,4]
target = 6
obj = Solution()
print(obj.twoSum(nums,target))