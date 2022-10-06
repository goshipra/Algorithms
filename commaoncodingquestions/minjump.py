#!/usr/bin/env python3
# minjump.py
# Author : Shipra

class Solution:
    def minJumps(self, arr, n):
        i = 0
        jump = 0

        while i < n-1:
            if (i + arr[i]) >= n -1:
                return jump + 1
            jumps  = 0
            for j in range(i,min(i + arr[i] + 1,n)):
                if (arr[j] + 1) >= jumps:
                    jumps = arr[j] + j
                    i = j
            jump += 1
        return jump


#code here


arr = [0,1,1,1,1]
n = 11
obj = Solution()
print(obj.minJumps(arr,n))