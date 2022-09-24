#!/usr/bin/env python3
# reverseString.py
# Author : Shipra

# def reverseString(string):
#     result = ''
#     for i in range(1,len(string)+1):
#         res = string[len(string) - i]
#         result += res
#     return result

def reverseString(string):

    result = "".join(reversed(string))

    return result



string = "kamal"
print(reverseString(string))
