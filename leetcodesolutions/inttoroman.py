#!/usr/bin/env python3
# inttoroman.py
# Author : Shipra


class Solution:
    """
    Given an integer num, convert it to a roman numeral.
    """

    VALUES = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    SYMBOLS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    def intToRoman(self, num):
        result = []
        for value, symbol in zip(self.VALUES, self.SYMBOLS):
            count, num = divmod(num, value)
            result.append(symbol * count)
        return "".join(result)


if __name__ == "__main__":
    n = 19
    print(Solution().intToRoman(n))
