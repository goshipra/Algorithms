#!/usr/bin/env python3
# removeChar.py
# Author : Shipra

InputString = 'amalagamant'
target = 'a'

if target in InputString:
    print(InputString.replace(target,''))
else:
    print("Not Found")

new_string =''
for element in InputString:
    if element == target:
        new_string = InputString.replace(target,'')   
    else:
        continue

print(new_string)         
