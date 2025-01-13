#!/usr/bin/env python3
# LongestSubstring.py
# Author : Shipra

class Solution(object):
    '''
    Given a string s, find the length of the longest substring without
    repeating characters.
    '''
    def lengthOfLongestSubstring(self, s):

        print(s)
        dictsub = {}
        strglist = []
        substring = ''
        for j in range(len(s)-1):
            i = j+1
            while i <= len(s)-1:
                if s[i] in dictsub:
                    break
                else:
                    dictsub[s[i]] = 1
                    substring = substring + s[i]
                i += 1
            strglist.append(substring)
        print(len(dictsub))
        print(strglist)


    # def lengthOfLongestSubstring(self, s):
    #     listSubstring = []
    #     lengthSubstring = []
    #
    #     if len(s) < 2:
    #         if len(s) == 0:
    #             return 0
    #         else:
    #             return len(s)
    #
    #     outputString = s[0]
    #     if len(s) == 2:
    #         if outputString == s[1]:
    #             return len(outputString)
    #         else:
    #             outputString = outputString + s[1]
    #             return len(outputString)
    #
    #     for i in range(1, len(s)):
    #         if s[i] in outputString:
    #
    #             # Work on this part
    #             if s[i] != s[i-1]:
    #                 previous_index = outputString.index(s[i])
    #                 oldSubstring = outputString
    #                 outputString = s[previous_index:] + s[i]
    #                 listSubstring.append(oldSubstring)
    #                 print(outputString)
    #                 print(listSubstring)
    #             else:
    #                 oldSubstring = outputString
    #                 outputString = s[i]
    #                 listSubstring.append(oldSubstring)
    #                 print(outputString)
    #                 print(listSubstring)
    #         else:
    #             outputString = outputString + s[i]
    #             listSubstring.append(outputString)
    #             print(outputString)
    #             print(listSubstring)
    #
    #     print(listSubstring)
    #     for item in listSubstring:
    #         lengthSubstring.append(len(item))
    #
    #     maximum_length = max(lengthSubstring)
    #     return maximum_length


s = 'AAAABDEFGAKTBEF'
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
