#!/usr/bin/env python3
# vowelConsonant.py
# Author : Shipra

def vowelConsonants(string):

    vowel = 0
    consonant = 0
    vowels = "aeiouAEIOU"
    for element in string:
        if element in vowels:
            vowel += 1
            print(vowel,element)
        else:
            consonant += 1
            print(consonant,element)

    return vowel, consonant

string = "AeIOu"
print(vowelConsonants(string))