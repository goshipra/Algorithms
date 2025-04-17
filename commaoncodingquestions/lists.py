# . Find the Maximum Number
# Description: Given a list of numbers, find and return
#  the largest number.

# Input: [3, 5, 2, 9, 1]

# Output: 9

def max_num(alist):
    maxn = alist[0]
    for i in range (1,len(alist)):
        if alist[i] > maxn:
            maxn = alist[i]
        else:
            continue
    return maxn        

print(max_num([3, 5, 2, 9, 1]))

# 2. Find the Minimum Number
# Description: Given a list of numbers, return the smallest one.

# Input: [8, 6, 3, 7, 2]

# Output: 2

def min_number(alist):
    alist = sorted(alist)
    min = alist[0]
    return min

print(min_number([8, 6, 3, 7, 2]))


# 3. Sum of All Elements
# Description: Return the sum of all numbers in the list.

# Input: [1, 2, 3, 4]

# Output: 10   


def sum_of_list(alsit):
    summ = 0
    for element in alsit:
        summ = summ + element
    return summ

print(sum_of_list([1, 2, 3, 4]))  

# 4. Count Even Numbers
# Description: Count how many even numbers are in the list.

# Input: [2, 5, 6, 9, 10]

# Output: 3

def even_count(alsit):
    count = 0
    for element in alsit:
        if element % 2 == 0.0:
            count += 1
        else:
            continue
    return count

print(even_count([5,7,9,10,2, 5]))  

# 5. Reverse a List
# Description: Return the list in reverse order.

# Input: [1, 2, 3, 4]

# Output: [4, 3, 2, 1]

import math
def reverse_list(alsit):

    j = len(alsit) -1

    for i in range(math.ceil(j/2)):
        alsit[i],alsit[j] = alsit[j],alsit[i]
        j -= 1
    return alsit

print(reverse_list([4, 3, 2, 1])) 

# 6. Find the Index of a Target Element
# Description: Given a list and a target value, return the index of the target
#  (or -1 if not found).

# Input: [4, 7, 2, 9], target = 2

# Output: 2


def find_index(alsit , target):

    for i in range(0,len(alsit)):
        if alsit[i] == target:
            return i
        else:
            continue
    return -1 
print(find_index([4, 7, 2, 9],9))   


# 7. Check for Duplicates
# Description: Return True if the list contains any duplicate elements, else False.

# Input: [1, 2, 3, 4, 2]

# Output: True

def duplicates(alsist):
    newList = []
    for element in alsist:
        if element in newList:
            return True
        else:
            newList.append(element)
    return False

print(duplicates([1, 2, 3, 4]))

# 8. Merge Two Lists
# Description: Given two lists, return a single list that combines them.

# Input: [1, 2] and [3, 4]

# Output: [1, 2, 3, 4]

def mergelists(list1, list2):
    for element in list2:
        list1.append(element)

    return list1

print(mergelists([1, 2], [3, 4]))
    
    
# 9. Remove Duplicates
# Description: Return a new list that contains only unique elements
#  from the original list.

# Input: [1, 2, 2, 3, 1]

# Output: [1, 2, 3]   

def uniquelist(list1):
    newlist = []
    for element in list1:
        if element in newlist:
            continue
        else:
            newlist.append(element)
    return newlist        

print(uniquelist([1, 2, 2, 3, 1]))

# 10. Check if List is Palindrome
# Description: Check if the list reads the same forward and backward.

# Input: [1, 2, 3, 2, 1]

# Output: True

def pallindrome(alist):
    j = len(alist) -1    # 4
    print(j)
    for i in range(0,j-1): #0-3
            if alist[i] == alist[j]:
                j -= 1
            else:
                return False
    return True             
               
print(pallindrome([1, 2, 3, 1]))   

# 11. Count Occurrences of a Number
# Description: Given a list and a target number, 
# count how many times it appears in the list.

# Input: [1, 2, 2, 3, 2], target = 2

# Output: 3

def count_num(alist,target):
    count = 0
    for element in alist:
        if element == target:
            count += 1
        else:
            continue
    return count
print(count_num([1, 2, 2, 3, 2], target = 2))        

# 12. Get All Positive Numbers
# Description: Return a new list containing only 
# the positive numbers from the original list.

# Input: [-1, 2, -3, 4, 0]

# Output: [2, 4]

def get_positives(alist):
    for element in alist:
        if element < 0:
            alist.remove(element)
            continue
    return alist

print(get_positives([-1, 2, -3, 4, 0])) 

# 13. Square Every Element
# Description: Return a new list where each element 
# is the square of the original.

# Input: [1, 2, 3]

# Output: [1, 4, 9]

def square(alist):
    newlist = []
    for element in alist:
        element = element ** 2
        newlist.append(element)
    return newlist
print(square([1, 2, 3])) 


# 14. Find Second Largest Element
# Description: Return the second largest number in the list.

# Input: [10, 20, 5, 8]

# Output: 10

def sec_largest(alist):
    largest = alist[0]
    sec_largest = alist[1]
    if largest < sec_largest:
        largest,sec_largest = sec_largest,largest

    for element in alist:
        if element < sec_largest:
            continue
        elif element > sec_largest and element > largest:
            largest = element
            sec_largest = largest
        elif   element > sec_largest and element < largest:
            sec_largest = element
        else:
            continue      

    return sec_largest

print(sec_largest([10, 20, 5, 8,16])) 

# 15. Find All Pairs with Given Sum
# Description: Return all pairs of elements that sum up to
#  a given target.

# Input: [1, 2, 3, 4, 5], target = 6

# Output: [(1, 5), (2, 4)]

def find_pairs(alist, target):
    pairs  = []
    for i in range(len(alist)):
        for j in range(i+1, (len(alist))):
            remains = target - alist[i]
            if remains == alist[j]:
                pairs.append((alist[i],alist[j]))
            else:
                continue
    return pairs

print(find_pairs([1, 2, 3, 4, 5 ,6,7,8,9 ], target = 10)) 

# 16. Rotate List Right by 1
# Description: Shift all elements one place to the right,
#  moving the last to the first position.

# Input: [1, 2, 3, 4 ]

# Output: [4, 1, 2, 3]

def roatatebyn(alist,n):
    newlist = alist[len(alist)-n:len(alist)] + alist[0:len(alist)-n]
    return newlist
print(roatatebyn( [1, 2, 3, 4 ,5 ,6,7 ],3))


# 17. Find Common Elements Between Two Lists
# Description: Return a list of elements that 
# appear in both lists.

# Input: [1, 2, 3], [2, 3, 4]

# Output: [2, 3]

def findcommon(alist, blist):
    common = []
    for element in alist:
        if element in blist:
            common.append(element)
        else:
            continue
    return common

print(findcommon([1, 2, 3], [2, 3, 4]))   

# 18. Flatten a 2D List
# Description: Convert a list of lists into a single 
# flattened list.

# Input: [[1, 2], [3, 4], [5]]

# Output: [1, 2, 3, 4, 5]

def flattenlist(alist):
    flatlist = []
    for element in alist:
        print(element)
        if isinstance(element,list):
            flatlist.extend(flattenlist(element))
        else:
            print("appending: ",element)
            flatlist.append(element)
    return flatlist
print(flattenlist([[1, 2], [3, 4], [5]]))  

# 19. Check if Two Lists are Identical
# Description: Return True if two lists have the same 
# elements in the same order.

# Input: [1, 2, 3], [1, 2, 3]

# Output: True

def identity(alist,blist):
    if len(alist) == len(blist):
        for i in range(len(alist)):
            if alist[i] != blist[i]:
                return False
            else:
                continue
        
    else:
        return False
    return True
print(identity([1, 2, 7], [1, 2, 3]))

# 20. Move Zeros to End
# Description: Move all zeros to the end of the list without
#  changing the order of non-zero elements.

# Input: [0, 1, 0, 3, 12]

# Output: [1, 3, 12, 0, 0]

def movezeros(alist):
    count = 0
    for element in alist:
        if element == 0:
            alist.remove(element)
            count += 1
        else:
            continue
    zerolist = []    
    for i in range(count):
        zerolist.append(0)
    return alist + zerolist
print(movezeros([0, 0,-1, 1, 0, 3, 12, 0]))        




 

    









        