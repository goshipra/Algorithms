#!/usr/bin/env python3
# roman.py
# Author : Shipra


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = { 'I' : 1,'V' : 5, 'X' : 10,'L' : 50,
        'C' : 100,'D' : 500,'M' : 1000}
        integer = 0
        if s in roman:
            return roman[s]

        for i in range(1,len(s)):
            if roman[s[i]] <= roman[s[i-1]]:
                integer = integer + roman[s[i-1]]
            else:
                integer = integer - roman[s[i-1]]
        integer = integer + roman[s[i]]

        return integer


s = "LVIII"
obj = Solution()
print(obj.romanToInt(s))





