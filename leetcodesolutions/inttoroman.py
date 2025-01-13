#!/usr/bin/env python3
# inttoroman.py
# Author : Shipra

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1, 4, 5, 9, 10, 40, 50, 90,
                100, 400, 500, 900, 1000]
        roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC",
                 "C", "CD", "D", "CM", "M"]

        if num in nums:
            ind = nums.index(num)
            return roman[ind]

        i = 12
        result = ''
        while num:
            print(i, ":i")
            quotient = num // nums[i]
            num = num % nums[i]
            print("quotient",quotient)
            while quotient:
                result = result + roman[i]
                quotient = quotient - 1
            i = i - 1
        return result


n = 19
obj = Solution()
print(obj.intToRoman(n))
