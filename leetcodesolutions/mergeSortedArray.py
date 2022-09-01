#!/usr/bin/env python3
# mergeSortedArray.py
# Author : Shipra

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(-m, 0, 1):
            nums1[i] = 0
        for j in range(n):
            nums1.remove(0)
            nums1.append(nums2[j])

        nums1.sort()
        print(nums1)



nums1 = [1]
m = 1
nums2 = []
n = 0
obj =Solution()
obj.merge(nums1, m, nums2, n)