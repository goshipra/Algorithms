#!/usr/bin/env python3
# .py
# Author : Shipra

class Solution:
    # Complete this function

    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        totalSum = sum(A)
        leftSum = 0

        for i in range(N):
            rightSum = totalSum - leftSum - A[i]
            if leftSum == rightSum:
                return i+1
            leftSum = leftSum + A[i]

        return -1


n = 7
A = [0,1,3,-2,-1]
obj = Solution()
print(obj.equilibriumPoint(A,n))