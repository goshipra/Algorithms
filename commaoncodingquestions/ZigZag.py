#!/usr/bin/env python3
# ZigZag.py
# Author : Shipra

# def ZigZag(arr,n):
#     if len(arr) % 2 != 0:
#         for i in range(1, len(arr), 2):
#             if arr[i] < arr[i + 1]:
#                 if arr[i - 1] < arr[i + 1]:
#                     arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 else:
#                     arr[i - 1], arr[i] = arr[i], arr[i - 1]
#             else:
#                 if arr[i] < arr[i - 1]:
#                     arr[i], arr[i - 1] = arr[i - 1], arr[i]
#     else:
#         for i in range(1, len(arr) - 1, 2):
#             print(arr[i])
#             if arr[i] < arr[i + 1]:
#                 if arr[i - 1] < arr[i + 1]:
#                     arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 else:
#                     arr[i - 1], arr[i] = arr[i], arr[i - 1]
#             else:
#                 if arr[i] < arr[i - 1]:
#                     arr[i], arr[i - 1] = arr[i - 1], arr[i]
#         if arr[i + 2] < arr[i + 1]:
#             arr[i + 2], arr[i + 1] = arr[i + 1], arr[i + 2]
#
#     return arr

class Solution:

    def zigZag(self, arr, n):
        if n <= 1:
            return arr

        newArr = sorted(arr)
        for i in range(1, n, 2):
            newArr[i], newArr[i + 1] = newArr[i + 1], newArr[i]

        return newArr


Inputarr = [6202, 4625, 5469, 2038, 5916 ,3405, 5533, 7004, 2469 ,9853, 4992, 361, 9819 ,3294 ,7195 ,4036 ,9404, 8767, 5404 ,1711 ,3214 ,3100 ,3751, 2139 ,5437 ,4993 ,1759 ,9572, 6270, 3789 ,9623, 2472 ,9493]
n = len(Inputarr)
obj = Solution()
print(obj.zigZag(Inputarr, n))
