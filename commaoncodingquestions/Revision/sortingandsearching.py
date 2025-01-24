# 4. Sorting and Searching
# Implement Bubble Sort, Insertion Sort, or Selection Sort.
# Write a binary search function.
# Merge two sorted lists into one sorted list.


def bubble_sort(Array):
    # if num[i] > num[i+1],
    #  then swap and i = i+1, 
    # else: i = i+1;
    lenth = len(Array)
    for j in range(lenth-1):
        for i in range(lenth-1):
            if Array[i] > Array[i+1]:
                Array[i],Array[i+1] = Array[i+1],Array[i]
            else:
                i = i + 1    
    print(Array)

my_list = [0,9,5,3,2,4,6,9]
bubble_sort(my_list)