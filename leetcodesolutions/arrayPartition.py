#!/usr/bin/env python3
# arrayPartition.py
# Author : Shipra

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for i in range(0,len(nums),2):
            res += nums[i]

        return res


nums = [6, 2, 6, 5, 1, 2]
obj = Solution()
print(obj.arrayPairSum(nums))
