#!/usr/bin/env python3
# pallindrome.py
# Author : Shipra

def pallindrome(string):

    result = ''
    for i in range(1,len(string)+1):
        res = string[len(string) - i]
        result += res

    if result == string:
        return True
    else:
        return False


string = "1234321"
print(pallindrome(string))