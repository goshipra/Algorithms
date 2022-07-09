#!/usr/bin/env python3
# ImplementstrStr.py
# Author : Shipra

class Solution(object):
    def strStr(self, haystack, needle):
        """
        Implement strStr()
        Given two strings needle and haystack, return the index of
        the first occurrence of needle in haystack, or -1 if needle is
         not part of haystack.
        """
        if needle == '':
            return 0
        # if needle in haystack:
        #     return haystack.index(needle)
        # else:
        #     return -1
        lenghtNeedle = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:i+lenghtNeedle]:
                return i

        return -1

haystack = 'hellolaopslola'
needle = 'lola'
obj = Solution()
print(obj.strStr(haystack,needle))
