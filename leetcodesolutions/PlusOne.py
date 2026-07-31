#!/usr/bin/env python3
# PlusOne.py
# Author : Shipra


class Solution:
    """
    Given a large integer represented as an array of digits, increment
    the integer by one and return the resulting array of digits.
    """

    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    digits = [0, 0, 0]
    print(Solution().plusOne(digits))
