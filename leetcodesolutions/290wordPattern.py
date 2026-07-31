#!/usr/bin/env python3
# 290wordPattern.py
# Author : Shipra


class Solution:
    """
    Given a pattern and a string s, find if s follows the same pattern,
    where a full match means there is a one-to-one mapping between a
    letter in pattern and a non-empty word in s.
    """

    def wordPattern(self, pattern, s):
        words = s.split()
        if len(words) != len(pattern):
            return False

        mapping = {}
        for i in range(len(pattern)):
            if pattern[i] not in mapping:
                mapping[pattern[i]] = words[i]
            elif mapping[pattern[i]] != words[i]:
                return False
        return True


if __name__ == "__main__":
    pattern = "aaa"
    s = "aa aa aa"
    print(Solution().wordPattern(pattern, s))
