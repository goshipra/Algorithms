#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 21 11:37:16 2022

@author: kamals
"""

def sequence(n):
    while(n!=1):
        print(n)
        if n % 2 == 0:
            n=n/2
            
        else:
            n=n*3+1
            
            
sequence(16)            
    
    