#!/usr/bin/env python3
# firstLastPosition.py
# Author : Shipra

class Solution(object):
    def searchRange(self, nums, target):
        '''
        Given an array of integers nums sorted in non-decreasing
         order, find the starting and ending position of a given
         target value. If target is not found in the array,
          return [-1, -1].You must write an algorithm with O(log n)
           runtime complexity.
           '''
        positions = [-1, -1]

        if target not in nums or nums == []:
            return positions
        else:
            first_index = nums.index(target)
            positions[0] = first_index

        if len(nums) == 1 and nums[0] == target:
            positions[0] = 0
            positions[1] = 0
            return positions

        if len(nums) == 2 and target in nums:
            if nums[0] == nums[1]:
                positions[0] = 0
                positions[1] = 1
                return positions
            else:
                if target == nums[0]:
                    positions[0] = 0
                    positions[1] = 0
                    return positions
                else:
                    positions[0] = 1
                    positions[1] = 1
                    return positions

        if nums[0] == nums[-1]:
            positions[0] = 0
            positions[1] = len(nums)-1
            return positions

        for i in range(-1,-len(nums)-1,-1):
            if nums[i] == target:
                positions[1] = len(nums) + i
                return positions
            else:
                continue

nums = [0,1,2,2,3]
target = 3
obj = Solution()
print(obj.searchRange(nums,target))
