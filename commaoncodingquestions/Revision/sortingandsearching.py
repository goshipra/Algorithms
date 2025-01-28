# 4. Sorting and Searching
# Implement Bubble Sort, Insertion Sort, or Selection Sort.
# Write a binary search function.
# Merge two sorted lists into one sorted list.

def bubble_sort(Array):
    lenth = len(Array)
    for j in range(lenth-1):
        for i in range(lenth-1):
            if Array[i] > Array[i+1]:
                Array[i],Array[i+1] = Array[i+1],Array[i]
            else:
                i = i + 1    
    print(Array)

my_list = [0,9,5,3,2,4,6,9]
# bubble_sort(my_list)



def insertion_sort(mylist):
    # first loop : second element to last, 
    # inner loops : n-1 till element is greater
    #  than that element. 
    for i in range(1,len(my_list)):
        for j in range(i-1,-1,-1):
            print(my_list)
            if my_list[i] <= my_list[j]:
                my_list[i],my_list[j] = my_list[j],my_list[i]
                i = i -1
            else:
                continue    

    print(my_list)

insertion_sort(my_list)

