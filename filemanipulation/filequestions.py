# 1. Read a File and Print Content
# Question:
# Write a program to read a text file and print its content 
# line by line.

# Input:
# A file named input.txt containing:
# Hello World  
# Welcome to file handling  
# Output:
# Hello World  
# Welcome to file handling 

def readandprint():
    with open ('afile.txt','r+t') as afile:
        print(afile.read())

# readandprint() 

# 2. Count Lines in a File
# Question:
# Write a program to count the number of lines in a
#  text file.

# Input:
# A file data.txt with the following content:
# Line 1  
# Line 2  
# Line 3  
# Output:
# 3
def count_lines():
    count = 0
    with open ('afile.txt','r+t') as afile:
        for x in afile:
            count += 1
    return count        

# print(count_lines())

# 3. Write List of Strings to File
# Question:
# Given a list of strings, write each string to a new line in 
# a file.

# Input:
# List: ["apple", "banana", "cherry"]

# Output in fruits.txt:
# apple  
# banana  
# cherry  

def string_to_file(alist,filename):
    with open (filename,"w") as afile:
        for element in alist:
            afile.write(element + "\n")

# string_to_file(["apple", "banana", "cherry"],'fruits.txt')

# 4. Append to a File
# Question:
# Append the line "New line added" to an existing file.

# Input:
# File log.txt contains:
# Line 1  
# Line 2  
# Output (updated file):
# Line 1  
# Line 2  
# New line added  

def append_to_file(filename,line):
    with open (filename,'a+t')as afile:
        afile.write('\n' +line)

# append_to_file('afile.txt',"This is new line")

def append_to_file(filename,alist):
    with open (filename,'a+t')as afile:
        for fruit in alist:
            afile.write('\n' + fruit)
# append_to_file('afile.txt',["apple","blueberry","cherries"])


# 5. Count Words in File
# Question:
# Write a program to count the number of words in a file.
# Input:
# File story.txt contains:
# Once upon a time there was a fox.  
# Output:
# 8

def count_words(filename):
    count = 0
    with open (filename,'r+t' ) as afile:
        for char in afile:
            count += 1
    return count
# print(count_words('fruits.txt'))   

# 6. Replace Word in File
# Question:
# Replace all occurrences of "apple" with "orange" in a file.

# Input:
# File fruits.txt:
# apple is red  
# apple is tasty  
# Output (modified file):
# orange is red  
# orange is tasty  

def replace_word(filename,word,replacement):
    with open (filename ,'r+') as afile:
        content = afile.read()

    new_content = content.replace(word,replacement)

    with open(filename,'w')  as afile:
        afile.write(new_content)
          
# replace_word("fruits.txt", "apple", "orange")  

def copy_content(filename,destnation):
    with open (filename,'r+') as afile:
        with open (destnation,'w') as bfile:
            bfile.write(afile.read())

copy_content("afile.txt","destniation.txt")             

             
# 8. Check if File Exists
# Question:
# Write a program to check whether a file myfile.txt 
# exists in the current directory.

# Input:
# myfile.txt exists.

# Output:
# File exists
import os
def check_file(filename): 
    if os.path.isfile(filename):
        print("File exists")
    else:
        print("File do not exist") 

# check_file("destniations.txt")

# 9. Find Longest Line in File
# Question:
# Find and print the longest line from a file.

# Input (text.txt):
# short  
# medium length  
# this is the longest line in the file  
# Output:
# this is the longest line in the file

def longest_line(filename):
    max = 0
    longestline = ''
    with open (filename,'r' ) as afile:
        for line in afile:
            if len(line) > max:
                max = len(line)
                longestline = line
            else:
                continue
    return longestline

# print(longest_line("afile.txt"))


# 10. Read File in Reverse
# Question:
# Print the contents of a file in reverse order (last line first).
# Input (reverse.txt):
# First line  
# Second line  
# Third line  
# Output:
# Third line  
# Second line  
# First line  

def reverse_read(filename):
    with open (filename, 'r') as afile:
        lines = afile.readlines()
        print(lines)
        for line in reversed(lines):
            print(line)

# reverse_read("fruits.txt")

# 11. Remove Blank Lines from a File
# Question:
# Write a program that removes all blank lines from a file.

def remove_blank_lines(filename):
    with open(filename,'r') as afile:
        content = afile.readlines()
        print(content)
        for line in content:
            if line == " '\n'":
                continue
            else:
                with open(filename , 'a') as afile:
                    afile.write(line)   

remove_blank_lines("afile.txt")           






































