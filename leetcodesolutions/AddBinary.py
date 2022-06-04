#!/usr/bin/env python3
# AddBinary.py
# Author : Shipra


class Solution(object):
    """
    Given two binary strings a and b, return
    their sum as a binary string.
    """
    def addBinary(self, a, b):
        OutputString = ''

        if len(a) != len(b):
            if len(a) > len(b):
                lenght = len(a) - len(b)
                b = '0' * lenght + b
            else:
                lenght = len(b) - len(a)
                a = '0' * lenght + a


        Stringlength = len(a) - 1
        carry = '0'
        for i in range(Stringlength,-1,-1):

            if carry == '1':
                if a[i] == '1' and b[i] == '1':
                    OutputString = '1' + OutputString
                    carry = '1'
                elif a[i] == '1' and b[i] == '0':
                    OutputString = '0' + OutputString
                    carry = '1'
                elif a[i] == '0' and b[i] == '1':
                    OutputString = '0' + OutputString
                    carry = '1'
                elif a[i] == '0' and b[i] == '0':
                    OutputString = '1' + OutputString
                    carry = '0'
            else:
                if a[i] == '0' and b[i] == '1':
                    OutputString = '1' + OutputString
                    carry = '0'
                elif a[i] == '1' and b[i] == '0':
                    OutputString = '1' + OutputString
                    carry = '0'
                elif a[i] == '1' and b[i] == '1':
                    OutputString = '0' + OutputString
                    carry = '1'
                elif a[i] == '0' and b[i] == '0':
                    OutputString = '0' + OutputString
                    carry = '0'


        if carry == '1':
            OutputString = '1' + OutputString

        return OutputString


a = '1010'
b = '1011'
obj = Solution()
print(obj.addBinary(a,b))