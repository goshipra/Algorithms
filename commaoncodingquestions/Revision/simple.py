# 2. Array/Lists
# Rotate an array by k positions.
# Find the intersection of two arrays.


# Find the largest and smallest elements in a list.

def largest_smallest(mylist):
    sorted_list = sorted(mylist)
    print("smallest :",sorted_list[0],"largest :",sorted_list[-1])

#largest_smallest([1,2,3,4,56,4,3,2]) 


# Write a program to remove duplicates from a list.

def remove_duplicate(mylist):
    newlist = []

    for element in mylist:
        if element in newlist:
            continue
        else:
            newlist.append(element)

    print(newlist) 

remove_duplicate([1,2,3,4,56,4,3,2])    
