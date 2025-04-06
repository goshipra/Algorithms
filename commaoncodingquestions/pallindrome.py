#!/usr/bin/env python3
# pallindrome.py
# Author : Shipra

class Solution():
    def isPalindrome(self, string):
        if len(string) <= 1:
            return True

        def cleanString(string):
            newstring = ''
            for element in string:
                if element.isalnum():
                    newstring = newstring + element.lower()
            print(newstring)
            return newstring

        string = cleanString(string)
        result = ''
        for i in range(1, len(string) + 1):
            res = string[len(string) - i]
            result += res

        if result == string:
            return True
        else:
            return False


string = ""
obj = Solution()
print(obj.isPalindrome(string))
