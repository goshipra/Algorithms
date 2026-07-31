#!/usr/bin/env python3
# MaxProfit.py
# Author : Shipra


class Solution:
    """
    Given an array prices where prices[i] is the price of a stock on
    day i, find the maximum profit from a single buy and a later sell.
    """

    def maxProfit(self, prices):
        left, right = 0, 1
        result = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                result = max(result, prices[right] - prices[left])
            else:
                left = right
            right += 1

        return result


if __name__ == "__main__":
    prices = [7, 6, 5, 4, 3, 2, 1]
    print(Solution().maxProfit(prices))
