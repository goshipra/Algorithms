#!/usr/bin/env python3
# Anagrams.py
# Author : Shipra


def Anagram(string1,string2):
    if len(string1) != len(string2):
        return False

    string1 = sorted(string1)
    string2 = sorted(string2)

    if string1 == string2:
        return True
    else:
        return False

string1 = "shipra"
string2 = "prashi"
print(Anagram(string1,string2))