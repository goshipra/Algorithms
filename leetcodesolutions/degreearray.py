#!/usr/bin/env python3
# degreearray.py
# Author : Shipra


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = {}
        for element in nums:
            if element in frequency:
                frequency[element] = frequency[element] + 1
            else:
                frequency[element] = 1
        print(frequency)
        print(max(frequency.values()))




nums = [1,2,2,2,3,1,1,1]
obj = Solution()
print(obj.findShortestSubArray(nums))