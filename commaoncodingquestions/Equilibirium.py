#!/usr/bin/env python3
# .py
# Author : Shipra

class Solution:
    # Complete this function

    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A):
        totalSum = sum(A)
        leftSum = 0

        for i in range(len(A)):
            rightSum = totalSum - leftSum - A[i]
            if leftSum == rightSum:
                return i+1
            leftSum = leftSum + A[i]

        return -1



A = [-7, 1, 5, 2, -4, 3, 0]
obj = Solution()
print(obj.equilibriumPoint(A))