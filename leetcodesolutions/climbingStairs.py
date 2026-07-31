#!/usr/bin/env python3
# climbingStairs.py
# Author : Shipra


class Solution:
    """
    You are climbing a staircase of n steps. Each time you can climb
    1 or 2 steps. Return the number of distinct ways to climb to the top.
    """

    def climbStairs(self, n):
        one, two = 1, 1
        for _ in range(n - 1):
            one, two = one + two, one
        return one


if __name__ == "__main__":
    print(Solution().climbStairs(4))
