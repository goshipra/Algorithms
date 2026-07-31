#!/usr/bin/env python3
# dominos.py
# Author : Shipra


class Solution:
    """
    Given two arrays of the same length tops and bottoms, in one swap
    you can pick i and swap tops[i] with bottoms[i]. Return the minimum
    number of swaps to make all values in tops the same, or all values
    in bottoms the same, or -1 if impossible.
    """

    def minDominoRotations(self, tops, bottoms):
        n = len(tops)

        def swaps_needed(target):
            top_swaps = bottom_swaps = 0
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                if tops[i] != target:
                    top_swaps += 1
                if bottoms[i] != target:
                    bottom_swaps += 1
            return min(top_swaps, bottom_swaps)

        result = swaps_needed(tops[0])
        if result != -1:
            return result
        return swaps_needed(bottoms[0])


if __name__ == "__main__":
    tops = [1, 2, 3, 4, 6]
    bottoms = [6, 6, 6, 6, 5]
    print(Solution().minDominoRotations(tops, bottoms))
