# 2. Find Key with Maximum Value
# Question: Find the key with the highest value in a dictionary.

# Input: {'a': 10, 'b': 25, 'c': 15}

# Output: 'b'
def max_value(adict):
    max = 0
    max_key = ''
    for elemnt in adict:
        if adict[elemnt] > max:
            max = adict[elemnt]
            max_key = elemnt
        else:
            continue    

    return max_key

print(max_value({'a': 10, 'i': 25, 'c': 15}))


# 1. Count Frequency of Elements
# Question:
# Given a list of integers, create a dictionary where keys 
# are the integers and values are their frequencies.

# Input:

# [1, 2, 2, 3, 1, 1]
# Output:

# {1: 3, 2: 2, 3: 1}

def count_values(alist):
    adict = {}
    for element in alist:
        if element in adict:
            adict[element] = adict[element] +1
        else:
            adict[element] = 1
    return adict

print(count_values([1, 2, 2, 3, 1, 1, 1]))        

# 2. Merge Two Dictionaries
# Question:
# Given two dictionaries, merge them into one.
#  If a key appears in both, the second dictionary’s
#  value should overwrite the first.

# Input:

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# Output:

# {'a': 1, 'b': 3, 'c': 4}

def merge_dict(adict, bdict):
    for element in bdict:
        adict[element] = bdict[element]    
    return adict

print(merge_dict({'a': 1, 'b': 2},{'b': 3, 'c': 4, 's': 8}))

# 4. Swap Keys and Values
# Question:
# Given a dictionary, return a new dictionary by swapping 
# keys and values.

# Input:
# {'x': 1, 'y': 2, 'z': 3}
# Output:
# {1: 'x', 2: 'y', 3: 'z'}

def swap(adict):
    new_dict = {}
    for elemnt in adict:
        new_dict[adict[elemnt]] = elemnt
    return new_dict
print(swap({'x': 1, 'y': 2, 'z': 3})) 

# 5. Check If Key Exists
# Question:
# Given a dictionary and a key, check whether the key exists.

# Input:
# {'apple': 5, 'banana': 7}, key = 'banana'
# Output:
# True

def check_key(adict,key):
    for element in adict:
        if element == key:
            return True
    return False

print(check_key({'apple': 5, 'banana': 7}, key = 'banana'))   


# 6. Sum All Values in Dictionary
# Question:
# Given a dictionary with numeric values, 
# return the sum of all values.

# Input:
# {'a': 10, 'b': 20, 'c': 5}
# Output:
# 35

def sumofvalues(adict):
    sumvalu = 0
    for element in adict:
        sumvalu = sumvalu + adict[element]
    return sumvalu

print(sumofvalues({'a': 10, 'b': 20, 'c': 5}))  


# 7. Filter Dictionary by Value Condition
# Question:
# From a dictionary, return a new dictionary where values
# are greater than a given threshold.

# Input:
# {'a': 10, 'b': 5, 'c': 20}, threshold = 10
# Output:
# {'c': 20}

def greaterthanthreshold(adict, threshold):
    greatervalues = {}
    for element in adict:
        if adict[element] > threshold:
            greatervalues[element] = adict[element]
        else:
            continue
    return greatervalues

print(greaterthanthreshold({'a': 10, 'b': 5, 'c': 20, 'd': 80}, threshold = 10))        


# 8. Create Dictionary from Two Lists
# Question:
# Given two lists of equal length, one of keys and 
# one of values, create a dictionary.

# Input:
# keys = ['name', 'age'], values = ['Alice', 25]
# Output:
# {'name': 'Alice', 'age': 25}

def create_dict(alist,blist):
    resdict = {}
    i = 0
    while i < len(alist):
        resdict[alist[i]] = blist[i]
        i += 1
    return resdict

print(create_dict(['name', 'age'],['Alice', 25]))


# 9. Group Words by First Letter
# Question:
# Group a list of words into a dictionary by their first letter.

# Input:
# ['apple', 'banana', 'apricot', 'blueberry']
# Output:
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

def grouping(alist):
    resdict = {}
    for element in alist:
        if element[0] in resdict:
            resdict[element[0]] = [resdict[element[0]], element]
        else:
            resdict[element[0]] = element
    return resdict

print(grouping(['apple', 'banana','avocado', 'apricot', 'blueberry','cherries']))  

# 10. Invert a Dictionary with List Values
# Question:
# Given a dictionary where values are lists,
# create a new dictionary where each item in those lists 
# becomes a key pointing to the original key.

# Input:
# {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}
# Output:
# {'apple': 'fruits', 'banana': 'fruits', 'carrot': 'vegetables'}

def invertcategories(adict):
    resdict = {}
    for element in adict:
        for j in adict[element]:
            resdict[j] = element
    return resdict        


print(invertcategories({'fruits': ['apple', 'banana','avocado'], 'vegetables': ['carrot','eggplant']}))


# 11. Remove Key from Dictionary
# Question:
# Given a dictionary and a key, remove the key from the dictionary
# if it exists.

# Input:
# {'a': 1, 'b': 2, 'c': 3}, key = 'b'
# Output:
# {'a': 1, 'c': 3}

def removekey(adict, key):
    resdict = {}
    for element in adict:
        if element == key:
            continue
        else:
            resdict[element] = adict[element]

    return resdict

print(removekey({'a': 1, 'b': 2, 'c': 3}, key = 'b'))

def popfunction(adict):
    print("pop fuction: ")
    adict.popitem()
    print(adict)
    adict.pop('a')
    print(adict)
    adict.items()
    print(adict)
    print(adict.keys())
    adict.update({"color": "White"})
    print(adict)
    print(adict.values())
    print(adict.get('c'))
    return adict
print(popfunction({'a': 1, 'b': 2, 'c': 3,'d':4,'e':5}))

# 12. Count Characters in a String
# Question:
# Given a string, return a dictionary with the count of each 
# character.

# Input:
# "banana"
# Output:
# {'b': 1, 'a': 3, 'n': 2}

def returncount(astring):
    resdict = {}
    for char in astring:
        if char in resdict:
            resdict[char] = resdict[char] + 1
        else:
            resdict[char] = 1
    return resdict

print(returncount("banana")) 

# 13. Find Common Keys in Two Dictionaries
# Question:
# Given two dictionaries, return a list of keys that appear
# in both.

# Input:
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4,'e': 5}
# Output:
# ['b']

def common_keys(adict,bdict):
    alist = []
    for element in adict:
        if element in bdict:
            alist.append(element)

    return alist

print(common_keys({'a': 1, 'b': 2},{'b': 3, 'c': 4}))

# 14. Sum Values with Same Key from Two Dictionaries
# Question:
# Given two dictionaries, sum the values of common keys
#  and keep all unique keys.

# Input:
# dict1 = {'a': 5, 'b': 10}
# dict2 = {'b': 7, 'c': 3}
# Output:
# {'a': 5, 'b': 17, 'c': 3}

def sum_values(adict,bdict):
    for element in adict:
        if element in bdict:
            adict[element] = adict[element] + bdict[element]
            bdict.pop(element)
        else:
            continue
    
    for element in bdict:
        adict[element] = bdict[element]

    return dict(sorted(adict.items()))

print(sum_values({'a': 5,'s':40, 'b': 10},{'b': 7, 'c': 3}))  
















    
            


