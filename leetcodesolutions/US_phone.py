#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# US_phone.py
# Author : Shipra

# Find lines that contain a US-style phone number (e.g. 123-456-7890).

import re

PHONE_PATTERN = re.compile(r"[1-9]\d{1,2}-\d{3}-\d{1,4}")

if __name__ == "__main__":
    sample_lines = [
        "John Doe 123-456-7890\n",
        "Jane Smith no phone listed\n",
        "Sam Lee 987-654-3210\n",
    ]

    for line in sample_lines:
        if PHONE_PATTERN.search(line):
            print(line, end="")
