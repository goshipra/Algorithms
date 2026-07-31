#!/usr/bin/env python3
# file_read_write.py
# Author : Shipra

# Demonstrates the common ways to read a file in Python.

with open("song.txt", "r") as f:
    text_content = f.read()  # reads the whole file as a single string

with open("song.txt", "r") as f:
    first_line = f.readline()  # reads just the first line

with open("song.txt", "r") as f:
    lines = f.readlines()  # reads all lines into a list
    print(lines)

with open("img.png", "rb") as f:
    image = f.read()  # binary read for non-text files
