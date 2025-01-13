#!/usr/bin/env python3
# mergeSortedArray.py
# Author : Shipra


class Solution(object):
    def merge(self, nums1, m, nums2, n):

        left, right = 0,0

        while left <= len(nums1):
            if left > len(nums1) - 1:
                break
            if nums1[left] < nums2[right]:
                if left >= m:
                    nums1[left] = nums2[right]
                    left += 1
                    right += 1
                else:
                    left += 1
            else:
                nums1[left],nums2[right] = nums2[right],nums1[left]
                left += 1
        print(nums1)




# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         for i in range(-m, 0, 1):
#             nums1[i] = 0
#         for j in range(n):
#             nums1.remove(0)
#             nums1.append(nums2[j])
#
#         nums1.sort()
#         print(nums1)



nums1 = [1,2,3,0,0,0]
# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
m = 3
nums2 = [2,5,6]
n = 3
obj =Solution()
obj.merge(nums1, m, nums2, n)