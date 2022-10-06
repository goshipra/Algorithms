#!/usr/bin/env python3
# mostfrequent.py
# Author : Shipra

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evencount = 0
        dict = {}

        for num in nums:
            if num % 2 != 0:
                continue
            else:
                if num in dict:
                    dict[num] = dict[num] + 1
                else:
                    dict[num] = 1
                evencount += 1

        if evencount == 0:
            return -1
        maximum = max(dict.values())
        value = {i for i in dict if dict[i]== maximum}
        return min(value)



nums = []
obj = Solution()
print(obj.mostFrequentEven(nums))