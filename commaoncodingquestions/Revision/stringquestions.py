

#String Manipulation




#Write a function to reverse a string without 
# using built-in functions.

def reverse(string):
    result = ""
    # Iterate over the input string in reverse order
    for char in string:
        result = char + result
        print(result)

#reverse("shipra")

#Check if a given string is a palindrome.

def pallindrome(string):
    result = ''
    for char in string:
        result = char + result

    if result == string:
        print("pallindrome") 
    else:
        print("not pallindrome")       

#pallindrome("kkkkkk")

#Find the first non-repeating character in a string.

def first_non_repeating(string):
    count = {}
    for char in string:
        if char in count:
            count[char] = count[char] + 1
        else:
            count[char] = 1
    #print(count)            

    for element in count:
        if count[element] == 1:
            return element    

element = first_non_repeating("aabbcc")
print(element)

#Count the number of vowels and consonants in a string.
def vowel_consonent(string):
    vowel = ['a','e','i','o','u']
    v_count = 0
    c_count = 0
    for char in string:
        if char in vowel:
            v_count = v_count + 1
        else:
            c_count = c_count + 1
    print("Vowel = ",v_count)
    print('Consonent = ', c_count)            

vowel_consonent("krishiv")




