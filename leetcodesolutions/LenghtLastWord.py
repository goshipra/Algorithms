#!/usr/bin/env python3
# LenghtLastWord.py
# Author : Shipra


class Solution:
    """
    Given a string s consisting of words and spaces, return the length
    of the last word in the string.
    """

    def lengthOfLastWord(self, s):
        return len(s.split()[-1])


if __name__ == "__main__":
    s = "luffy is still joyboy"
    print(Solution().lengthOfLastWord(s))
