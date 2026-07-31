#!/usr/bin/env python3
# ImplementstrStr.py
# Author : Shipra


class Solution:
    """
    Given two strings needle and haystack, return the index of the
    first occurrence of needle in haystack, or -1 if needle is not
    part of haystack.
    """

    def strStr(self, haystack, needle):
        if needle == "":
            return 0

        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i

        return -1


if __name__ == "__main__":
    haystack = "hellilaopslila"
    needle = "lila"
    print(Solution().strStr(haystack, needle))
