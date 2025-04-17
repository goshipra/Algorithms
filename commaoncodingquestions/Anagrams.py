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

def Anagram(string1,string2):

    dict = {}

    for i in range(len(string1)):
        if string1[i] in dict:
            dict[string1[i]] = dict[string1[i]] + 1
        else:
            dict[string1[i]] = 1

    print(dict)        

    for j in range(len(string2)):
        if string2[j] in dict:
            dict[string2[j]] = dict[string2[j]] - 1
        else:
            dict[string2[j]] = 1
    print(dict)         
    maximum = max(dict.values())
    if maximum == 0:
        return True
    else:
        return False


string1 = "kamal"
string2 = "lamak"
print(Anagram(string1,string2))


