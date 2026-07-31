#!/usr/bin/env python3
# 205Isomorphic.py
# Author : Shipra


class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings are isomorphic if the characters in s can be replaced
    to get t, with a consistent one-to-one mapping.
    """

    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        mapping = {}
        for i in range(len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
            elif mapping[s[i]] != t[i]:
                return False
        return True


if __name__ == "__main__":
    s = "add"
    t = "mef"
    print(Solution().isIsomorphic(s, t))
