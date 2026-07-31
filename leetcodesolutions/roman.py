#!/usr/bin/env python3
# roman.py
# Author : Shipra


class Solution:
    """
    Given a roman numeral string s, convert it to an integer.
    """

    ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s):
        if s in self.ROMAN:
            return self.ROMAN[s]

        total = 0
        for i in range(len(s) - 1):
            if self.ROMAN[s[i]] < self.ROMAN[s[i + 1]]:
                total -= self.ROMAN[s[i]]
            else:
                total += self.ROMAN[s[i]]
        total += self.ROMAN[s[-1]]

        return total


if __name__ == "__main__":
    s = "LVIII"
    print(Solution().romanToInt(s))
