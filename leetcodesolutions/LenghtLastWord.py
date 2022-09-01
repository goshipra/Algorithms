#!/usr/bin/env python3
# LengthLastWord.py
# Author : Shipra


class Solution(object):
    def lengthOfLastWord(self, s):
        """
            find lenth of last word in a sentence
        """
        result = 0
        newString = s.strip()

        for c in reversed(newString):
            if c == ' ':
                break
            else:
                result += 1

        return result


s ="luffy is still joyboy"
obj = Solution()
print(obj.lengthOfLastWord(s))