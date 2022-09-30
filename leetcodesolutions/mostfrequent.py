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
        print(dict)
        if evencount == 0:
            return -1
        else:

            return min(dict)



nums = [1,2,2,4,4,6,4,6]
obj = Solution()
print(obj.mostFrequentEven(nums))