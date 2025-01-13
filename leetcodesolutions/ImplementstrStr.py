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

        lenghtNeedle = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:i+lenghtNeedle]:
                return i

        return -1

haystack = 'hellilaopslila'
needle = 'lila'
obj = Solution()
print(obj.strStr(haystack,needle))
