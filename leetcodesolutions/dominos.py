#!/usr/bin/env python3
# dominos.py
# Author : Shipra


class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        top = tops[0]
        tswap = 0
        i = 1
        while i <= len(tops)-1:
            if tops[i] == top:
                i = i + 1
            elif bottoms[i] == top:
                tswap = tswap + 1
                tops[i],bottoms[i] = bottoms[i],tops[i]
                i = i + 1
            else:
                break

        if tops.count(top) < len(tops):
            if bottoms.count(bottoms[0]) < len(tops):
                return -1
            else:
                return tswap
        else:
            return tswap



tops=   [1,2,3,4,6]
bottoms=[6,6,6,6,5]

obj = Solution()
print(obj.minDominoRotations(tops, bottoms))
