#!/usr/bin/env python3
# countCharacter.py
# Author : Shipra

def countCharacter(string,char):
    count = 0
    for i in range(0,len(string)):
        if string[i] == char:
            count += 1
        else:
            continue
    return count


string = "shipra"
print(countCharacter(string,'p'))