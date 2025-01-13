#!/usr/bin/env python3
# mostfrequent.py
# Author : Shipra

class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        evendict = {}
        if len(nums) == 0:
            return -1

        for num in nums:
            if num % 2 != 0:
                continue
            else:
                if num in evendict:
                    evendict[num] = evendict[num] + 1
                else:
                    evendict[num] = 1

        print(evendict)
        if len(evendict) == 0:
            return -1
        maximum = max(evendict.values())
        maxlist = []
        for key in evendict:
            if evendict[key] == maximum:
                maxlist.append(key)

        return min(maxlist)





nums = [0,1,2,2,4,4,1]
obj = Solution()
print(obj.mostFrequentEven(nums))
