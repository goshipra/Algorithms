#!/usr/bin/env python3
# LongestSubstring.py
# Author : Shipra


class Solution:
    """
    Given a string s, find the length of the longest substring without
    repeating characters.
    """

    def lengthOfLongestSubstring(self, s):
        seen = {}
        start = 0
        longest = 0

        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch] + 1
            seen[ch] = i
            longest = max(longest, i - start + 1)

        return longest


if __name__ == "__main__":
    s = "AAAABDEFGAKTBEF"
    print(Solution().lengthOfLongestSubstring(s))
