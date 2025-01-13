#!/usr/bin/env python3
# firstLastPosition.py
# Author : Shipra

class Solution(object):
    def searchRange(self, nums, target):
        '''
        Given an array of integers nums sorted in incresing
         order, find the starting and ending position of a given
         target value. If target is not found in the array,
          return [-1, -1].You must write an algorithm with O(log n)
           runtime complexity.
           '''
        positions = [-1, -1]
        indexes = []

        left = 0
        right = len(nums)-1

        if nums[right] < target:
            return positions

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                if mid == 0:
                    indexes.append(mid)
                if nums[mid-1] < target:
                    indexes.append(mid)
                    break
            if nums[mid] == target and nums[mid-1] == target:
                right = mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = indexes[0]
        right = len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                if mid == len(nums)-1:
                    indexes.append(mid)
                    break
                elif nums[mid+1] > target:
                    indexes.append(mid)
                    break
            if nums[mid] == target and nums[mid+1] == target:
                left = mid + 1
            else:
                right = mid - 1

        print("Both Pointers: ",indexes)
        return indexes


# class Solution(object):
#     def searchRange(self, nums, target):
#         '''
#         Given an array of integers nums sorted in incresing
#          order, find the starting and ending position of a given
#          target value. If target is not found in the array,
#           return [-1, -1].You must write an algorithm with O(log n)
#            runtime complexity.
#            '''
#         positions = [-1, -1]
#
#         if target not in nums or nums == []:
#             return positions
#         else:
#             first_index = nums.index(target)
#             positions[0] = first_index
#
#         if len(nums) == 1 and nums[0] == target:
#             positions[0] = 0
#             positions[1] = 0
#             return positions
#
#         if len(nums) == 2 and target in nums:
#             if nums[0] == nums[1]:
#                 positions[0] = 0
#                 positions[1] = 1
#                 return positions
#             else:
#                 if target == nums[0]:
#                     positions[0] = 0
#                     positions[1] = 0
#                     return positions
#                 else:
#                     positions[0] = 1
#                     positions[1] = 1
#                     return positions
#
#         if nums[0] == nums[-1]:
#             positions[0] = 0
#             positions[1] = len(nums)-1
#             return positions
#
#         for i in range(-1,-len(nums)-1,-1):
#             if nums[i] == target:
#                 positions[1] = len(nums) + i
#                 return positions
#             else:
#                 continue

nums = [1,2,3,3,3,3,3,3,5,6]
target = 3
obj = Solution()
print(obj.searchRange(nums,target))
