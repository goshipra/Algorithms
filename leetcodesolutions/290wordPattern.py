#!/usr/bin/env python3
# 290wordPattern.py
# Author : Shipra

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        new_dict = {}

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in new_dict:
                new_dict[pattern[i]] = words[i]
            else:
                if new_dict[pattern[i]] == words[i]:
                    continue
                else:
                    return False
        return True

        # words_list = s.split()
        # if len(words_list) != len(pattern):
        #     return False
        # dict = {}
        # for i in range(len(pattern)):
        #     print(dict)
        #     if pattern[i] in dict:
        #         if dict[pattern[i]] != words_list[i]:
        #             return False
        #         else:
        #             continue
        #     else:
        #         if words_list[i] in dict.values():
        #             return False
        #         dict[pattern[i]] = words_list[i]
        # return True


pattern = "aaa"
s = "aa aa aa"
obj = Solution()
print(obj.wordPattern(pattern,s))