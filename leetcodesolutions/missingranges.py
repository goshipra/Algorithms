#!/usr/bin/env python3
# missingranges.py
# Author : Shipra

# LeetCode 163. Missing Ranges — given a sorted integer array nums, where
# the range of elements are in the inclusive range [lower, upper], return
# its missing ranges.
#
# Example:
# Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
# Output: ["2", "4->49", "51->74", "76->99"]


class Solution:
    def missingranges(self, nums, lower, upper):
        if not nums:
            return [f"{lower} -> {upper}"]

        if nums[0] != lower:
            nums = [lower - 1] + nums
        if nums[-1] != upper:
            nums = nums + [upper + 1]

        result = []
        for i in range(len(nums) - 1):
            gap_start = nums[i] + 1
            gap_end = nums[i + 1] - 1
            if gap_start == gap_end:
                result.append(str(gap_start))
            elif gap_start < gap_end:
                result.append(f"{gap_start} -> {gap_end}")

        return result


if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(Solution().missingranges(nums, lower, upper))
