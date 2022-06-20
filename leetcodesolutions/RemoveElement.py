#!/usr/bin/env python3
# RemoveElements.py
# Author : Shipra

class Solution(object):
    def removeElement(self, nums, val):
        """
        Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
        Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
        """
        count = 0
        i = 0
        for elements in nums:
            if nums[i] == val:
                nums.remove(val)
                nums.append(val)
            else:
                count += 1
                i += 1
        return count


nums = [3,2,2,3]
val = 3
obj = Solution()
print(obj.removeElement(nums,val))
