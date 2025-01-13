#!/usr/bin/env python3
# rotatearray.py
# Author : Shipra


def rotateArray(k, arr):
    """rotate the array to the right by k steps, where k is non-negative
    """
    # for j in range(k):
    #     for i in range(0,len(arr)):
    #         arr[i] = arr[i] - 1
    #         if arr[i] == 0:
    #             arr[i] = len(arr)
    #
    # print(arr)

    for i in range(0,len(arr)):
        if arr[i] <= k:
            val = arr[i] - k
            arr[i] = len(arr) + val
        else:
            arr[i] = arr[i] - k

    print(arr)

def rotateUnsorted(k,arra):
    """rotate unsorted array k times
    ['s','h','i','p','r','a'] -> k=1
    ['a','s','h','i','p','r']
    ['s','h','i','p','r','a']  -> k=3
    ['p','r','a','s','h','i']
    """
    if k > len(arra):
        k = k - len(arra)
    temp = -k
    temp2 = 0
    res =[]
    for i in range(0,len(arra)):
        if i < k:
            res.append(arra[temp])
            temp += 1
        else:
            res.append(arra[temp2])
            temp2 += 1
    print(res)

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(Array,i,j):
            while i <= j:
                Array[i],Array[j] = Array[j],Array[i]
                i += 1
                j -= 1
            return Array

        print(reverse(nums,0,k))
        print(reverse(nums,k,len(nums)-1))
        print(reverse(nums,0,len(nums)-1))



nums = [-1,-100,3,99]
k = 2
obj = Solution()
obj.rotate(nums,k)
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# k = 2
# rotateArray(k, arr)
# arra = ['s','h','i','p','r','a']
# k = 0
# rotateUnsorted(k,arra)
