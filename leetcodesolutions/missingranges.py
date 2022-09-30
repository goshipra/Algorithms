#!/usr/bin/env python3
# missingranges.py
# Author : Shipra

# LeetCode — 163. Missing Ranges Given a sorted integer array nums, where the range of elements are in the inclusive
# range [lower, upper], return its missing ranges.
#
# Example:
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]

class Solution():
    def missingranges(self, nums, lower, upper):
        reslist = []
        if len(nums) == 0:
            reslist.append(str(lower) + '->'+ str(upper))
            return reslist

        if nums[0] != lower:
            nums = [lower - 1] + nums
        if nums[-1] != upper:
            nums = nums + [upper + 1]
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i + 1] - 1:
                if nums[i] + 1 != nums[i + 1] - 1:
                    strin = str(nums[i] + 1) + '->' + str(nums[i + 1] - 1)
                    reslist.append(strin)
                else:
                    strin = str(nums[i] + 1)
                    reslist.append(strin)
            i += 1

        return reslist


nums = [45]
lower = 0
upper = 99
ranges = Solution()
print(ranges.missingranges(nums, lower, upper))
