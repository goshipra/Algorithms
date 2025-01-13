#!/usr/bin/env python3
# 205Isomorphic.py
# Author : Shipra

class Solution(object):
    def isIsomorphic(self, s, t):
        newdict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in newdict:
                newdict[s[i]] = t[i]
            else:
                if newdict[s[i]] == t[i]:
                    continue
                else:
                    return False
        return True

    # def isIsomorphic(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     if len(s) != len(t):
    #         return False
    #
    #     dict = {}
    #     for i in range(len(s)):
    #         print(dict)
    #         if s[i] in dict:
    #             if dict[s[i]] != t[i]:
    #                 return False
    #             else:
    #                 continue
    #         else:
    #             if t[i] in dict.values():
    #                 return False
    #             dict[s[i]] = t[i]
    #
    #     return True


s = "add"
t = "mef"
obj = Solution()
print(obj.isIsomorphic(s, t))


