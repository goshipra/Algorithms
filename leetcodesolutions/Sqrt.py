#!/usr/bin/env python3
# Sqrt.py
# Author : Shipra


class Solution:
    """
    Given a non-negative integer x, compute and return the square root
    of x, truncated to the integer part. Built-in exponent operators
    are not used.
    """

    def mySqrt(self, x):
        start, end = 0, x

        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                start = mid
            else:
                end = mid

        if end * end == x:
            return end
        return start


if __name__ == "__main__":
    target = 4
    print(Solution().mySqrt(target))
