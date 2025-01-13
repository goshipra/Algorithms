#!/usr/bin/env python3
# MaxProfit.py
# Author : Shipra

class Solution(object):
    def maxProfit(self, prices):
        """
        find Maximum profit
        """
        left , right = 0,1
        result = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                result = max(result, profit)
            else:
                left = right
            right += 1

        return result





prices =[7,6,5,4,3,2,1]
 # [7,1,5,3,6,4]
# [2,4,1]
obj = Solution()
print(obj.maxProfit(prices))


# MaxValue = 0
# for i in range(0,len(prices)):
#     for j in range(len(prices)-1,i,-1):
#         if prices[i] > prices[j]:
#             continue
#         else:
#             NewMaxValue = prices[j] - prices[i]
#             if NewMaxValue > MaxValue:
#                 MaxValue = NewMaxValue
#
# return MaxValue