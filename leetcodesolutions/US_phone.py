#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 15:08:28 2022

@author: kamals
"""

import sys # for input and output
import re #

pattern1="[1-9]\d{1,2}\-[0-9][0-9][0-9]\-\d{1,4}"

with open('names.txt') as f:
    lines = f.readlines()
    
    regexp = re.compile(pattern1)
    for line in lines:
        result = regexp.search(line)
        if result:
            sys.stdout.write(line)
            