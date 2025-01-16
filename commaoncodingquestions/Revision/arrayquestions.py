#Array/Lists

#Find the largest and smallest elements in a list.

def largest_smallest(lis):
   mylist = sorted(lis)
   print(mylist[0])
   print(mylist[-1])

#largest_smallest([1,2,3,4,5,6,7])

#Write a program to remove duplicates from a list.

def remove_duplicates(mylist):
    result = []
    for element in mylist:
        if element in result:
            continue
        else:
            result.append(element)
    print(result)         

mylist = [1,4,2,6,7,5,4,3,21,1]
#remove_duplicates(mylist)  


#Rotate an array by k positions.

def rotate_by_k(mylist, k):
    print(mylist, k)
    print(mylist[-k:] + mylist[:-k] )
    
#rotate_by_k(mylist,1)  


#Find the intersection of two arrays.

def intersection(mylist,list_b):
    result=[]
    for element in mylist:
        if element in list_b:
            result.append(element)
        else:
            continue    
    
    new_list = []
    for element in result:
        if element in new_list:
            continue
        else:
            new_list.append(element)
    print(new_list)        

list_b = [1,2,3,4]
intersection(mylist,list_b)


    

    









