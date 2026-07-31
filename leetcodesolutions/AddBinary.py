#!/usr/bin/env python3
# AddBinary.py
# Author : Shipra


class Solution:
    """
    Given two binary strings a and b, return their sum as a binary string.
    """

    def addBinary(self, a, b):
        a, b = a[::-1], b[::-1]
        result = []
        carry = 0

        for i in range(max(len(a), len(b))):
            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0
            total = bit_a + bit_b + carry
            result.append(str(total % 2))
            carry = total // 2

        if carry:
            result.append("1")

        return "".join(reversed(result))


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))
