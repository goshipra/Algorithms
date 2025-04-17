# Array and String
# Two Sum – Find two numbers that add up to a target.

def twosum(target):
    first_num = target/2
    sec_num = target - first_num
    print("this is first number",first_num,"and this is second number",sec_num,"there sum is ",first_num+sec_num)

#twosum(45)

# Remove Duplicates from Sorted Array

def remove_duplicates(array):
    new_array = []
    for element in array:
        if element in new_array:
            continue
        else:
            new_array.append(element)
    print(new_array)    

# remove_duplicates([1,1,2,2,3,3,4,4,5,6,7,8,8,9,9])


# Merge Two Sorted Arrays
def merge_array(list1,list2):
    ptr1 = 0
    ptr2 = 0
    res = []
    while ptr1 < len(list1):
        print(ptr1,ptr2)
        if list1[ptr1] <+ list2[ptr2]:
            ptr1 += 1
            res.append(list1[ptr1])
        else:
             res.append(list2[ptr2])  
             ptr2 += 1
    print(res)
    
# merge_array([1,2,3,4,5],[1,2,3,4])

# Maximum Subarray (Kadane’s Algorithm - optional)


# Reverse a String or Array

# Check for Anagram – Are two strings anagrams?

# Palindrome String – Is the string a palindrome?

# Implement strStr() / Substring Search