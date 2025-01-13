#!/usr/bin/env python3
# 344ReverseString.py
# Author : Shipra


#
# class Solution(object):
#     def reverseString(self, s):
#
#         for i in range(len(s)//2):
#             s[i],s[-i -1] = s[-i -1],s[i]
#         print("".join(s))

class Solution(object):
    def reverseString(self, s):
        news = s[:5]
        backs = s[5:]
        for i in range((len(news)//2)):
            news[i],news[-i-1] = news[-i-1],news[i]
        print("".join(news+backs))
        print(("".join(news+backs))[-1::-1])

        # """
        # :type s: List[str]
        # :rtype: None Do not return anything, modify s in-place instead.
        # """
        # string = "shipra"
        # print(string[-1::-1])
        # i = 0
        # j = -1
        # while i != len(s) // 2:
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1
        # print(s)



s = ["s","h","i","p","o","r","y","g"]
obj = Solution()
obj.reverseString(s)
