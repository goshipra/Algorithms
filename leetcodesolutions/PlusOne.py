#!/usr/bin/env python3
# PlusOne.py
# Author : Shipra

class Solution(object):
    def plusOne(self, digits):
        """
        plus one in digit
        """
        result = map(str, digits)
        result = "".join(result)
        result = int(result) + 1
        result = list(map(int, str(result)))

        return result


digits = [0, 0, 0]
obj = Solution()
print(obj.plusOne(digits))
