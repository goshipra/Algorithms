# 1. Reverse a String
# Question: Reverse the input string.

# Input: "hello"

# Output: "olleh"

def reverseString(astring):
    result = ''
    for i in range(len(astring)-1,-1,-1):
        result = result + astring[i]
    print(result)    
        
reverseString("hello") 

# 2. Check for Palindrome
# Question: Check if the given string is a palindrome 
# (reads the same forward and backward).

# Input: "racecar"

# Output: True

def pallindrome(astring):
    res = ''
    astring = astring.lower()
    for i in range(len(astring)-1,-1,-1):
        res = res + astring[i].lower()
    if res == astring:
        return True
    else:
        return False

print(pallindrome("Shihs")) 

# 3. Count Vowels in a String
# Question: Count the number of vowels (a, e, i, o, u) in the input string.

# Input: "apple"

# Output: 2

def countvowel(astring):
    count = 0
    astring = astring.lower()
    vowel = ['a','e','i','o','u']
    for char in astring:
        if char in vowel:
            count += 1
        else: 
            continue
    return count

print(countvowel("aRURPOuveiu")) 

# 4. Remove Duplicates from String
# Question: Remove duplicate characters from a string while maintaining order.

# Input: "banana"

# Output: "ban"

def removeduplicates(astring):
    res = ''
    for char in astring:
        if char in res:
            continue
        else:
            res = res + char
    return res
print(removeduplicates("banananabatasd")) 


# 5. Check Anagram
# Question: Check if two strings are anagrams 
# (contain the same letters in any order).

# Input: "listen", "silent"

# Output: True

def anagram(astring,bstring):
    dict = {}
    for char in astring:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
    print(dict)
    for char in bstring:
        if char in dict:
            dict[char] = dict[char] - 1
        else:
            dict[char]  = 1
    print(dict)
    maxvalue = max(dict,key=dict.get)
    maxv = dict[maxvalue]
    if maxv == 0:
        return True
    else:
        return False

print(anagram( "listen", "silyent"))

# 6. Find First Non-Repeating Character
# Question: Return the first character that does not 
# repeat in the string.

# Input: "swiss"

# Output: "w"

def non_repeating(astring):
    dict = {}
    for element in astring:
        if element in dict:
            dict[element] = dict[element] + 1
        else:
            dict[element] = 1
    for element in dict:
        if dict[element] == 1:
            return element
    return False    
        
print(non_repeating("sshipraipra"))

# 7. Replace All Spaces with Hyphens
# Question: Replace all spaces in a string with hyphens.

# Input: "hello world"

# Output: "hello-world"

def replacewithhyphen(astring):

    for element in astring:
        if element == ' ':
            astring = astring.replace(element,'-')
    return astring 

print(replacewithhyphen("he llo wor ld"))   

# 8. Check if String is Pangram
# Question: Check if a string contains every letter of the
#  alphabet at least once.

# Input: "The quick brown fox jumps over the lazy dog"

# Output: True

def pangram(astring):
    astring = astring.lower()
    alist = []
    for element in astring:
        if element in alist or element == ' ':
            continue
        else:
            alist.append(element)       
    
    if len(alist) == 26:
        return True
    
    return False

print(pangram("The quick brown fox jumps over the lazy dog"))

# 9. Count Words in a String
# Question: Count the number of words in a string. 
# Words are separated by spaces.

# Input: "I am learning Python"

# Output: 4

def countwords(astring):
    count = 1
    for element in astring:
        if element == ' ':
            count += 1
        else:
            continue
    return count

print(countwords("I am learning Python")) 

# 10. Capitalize First Letter of Each Word
# Question: Capitalize the first letter of every word in 
# the string.

# Input: "good morning shipra"

# Output: "Good Morning" 
# 

def capitalize(astring):
    newstring = astring[0].upper()
    i = 1
    while i < len(astring):
        if astring[i] == ' ':
            i += 1
            newstring = newstring + ' '+ astring[i].upper()
            i += 1
        else:
            newstring = newstring + astring[i]
            i +=1    
    return newstring

print(capitalize("good morning shipra rathore!"))  

# 11. Compress a String (Basic Run-Length Encoding)
# Question: Compress the string by replacing repeated 
# characters with the character followed by the count.

# Input: "aaabbc"

# Output: "a3b2c1"

def compresstodigit(astring):
    dict = {}
    for element in astring:
        if element in dict:
            dict[element] = dict[element] + 1
        else:
            dict[element] = 1

    newstring = ''
    for element in dict:
        newstring = newstring + element +str(dict[element]) 

    return newstring 

print(compresstodigit("aaabbcrrrrraaaaa"))    


# 12. Check if Two Strings are Rotations
# Question: Check if one string is a rotation of another.

# Input: "abcde", "deabc"

# Output: True

def rotations(astring, bstring):
    com = astring + astring
    print(com)

    if bstring in com:
        return True
    else:
        return False 

print(rotations("abcde", "stru"))

# 3. Remove All Digits
# Question: Remove all numeric digits from the string.

# Input: "abc123def"

# Output: "abcdef"

def removedig(astring):

    for element in astring:
        print(element)
        if element.isdigit():
            astring = astring.replace(element,'')
        else:
            continue    
    return astring

print(removedig("abc123def567"))    


# 14. Toggle Case of Each Character
# Question: Convert uppercase letters to lowercase and 
# vice versa.

# Input: "HeLLo"

# Output: "hEllO"

def toggle(astring):
    for element in astring:
        if element.islower():
            astring = astring.replace(element,element.upper())
        else:
            astring = astring.replace(element,element.lower())
    return astring

print(toggle("HeLLo"))  

# 15. Find Longest Word in a Sentence
# Question: Return the longest word from a sentence.

# Input: "I love programming"

# Output: "programming"

def longestword(astring):
    lst = astring.split()
    max = 0
    word =''
    for element in lst:
        if len(element) < max:
            continue
        else:
            max = len(element)
            word = element

    return word        

print(longestword("I love programming python-coder"))
    







        
        





                








        






