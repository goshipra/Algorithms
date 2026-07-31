#!/usr/bin/env python3
# 344ReverseString.py
# Author : Shipra


class Solution:
    """
    Reverse a string in place, represented as a list of characters.
    """

    def reverseString(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    s = ["s", "h", "i", "p", "o", "r", "y", "g"]
    Solution().reverseString(s)
    print(s)
