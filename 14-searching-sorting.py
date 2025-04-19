##################################################
# LINEAR SEARCH & BINARY SEARCH (logic)
#
# Binary search is a better way of searching an element in a long list may be having 1000 elements and so. It saves time.
# If you use linear search in such case and your element in at index 800, then we are wasting so much time in checking 800 elements.
#
# Prerequisite to use Binary Search:
#   * list must be sorted
#
##################################################


 LINEAR SEARCH
'''
index=-1

# def linear_search(list, item):
#     i=0
#     while i<len(list):
#         if list[i]==item:
#             # global index
#             # index=i
#             # OR
#             globals()['index'] = i
#             return True
#         i += 1
#     return  False

def linear_search(list,item):
    for i in range(len(list)):
        if list[i]==item:
            globals()['index'] = i
            return True
    return False

list = [5,8,4,6,9,2]
item = 9

if linear_search(list, item):
    print("found at ",index+1)
else:
    print("not found")
'''


# BINARY SEARCH
'''
index=-1

def binary_search(list,item):
    l=0
    u=len(list)-1

    # for i in range(len(list)):
    # OR
    while l<=u:
        mid = (l + u) // 2

        if item==list[mid]:
            globals()['index'] = mid
            return True
        elif item<list[mid]:
            u=mid
        else:
            l=mid

    return False

list = [2,5,8,33,66,88,97]
item = 88

if binary_search(list,item):
    print("found at position: ", index+1)
else:
    print("not found")
'''



####################################################
# SORTING: BUBBLE & SELECTION SORT
#
# - all sorting techniques use the concept of swapping
#
# BUBBLE SORT: [1,7,3,2]
# - iteration 1: [1,7,3,2]  [1,3,7,2]   [1,3,2,7]   -   largest item at end
# - iteration 2: [1,3,2,7]  [1,2,3,7]               -   last 2 items sorted
# - iteration 3: [1,2,3,7]                          -   last 3 items sorted
#
# SELECTION SORT: [1,7,3,2]
# - swapping consumes a lot of processing power, and in bubble sort it was everytime swapping in each iteration.
# - we want to do swapping only once, to save our cpu and memory, this is where selection sort comes into picture.
# - in selection sort, we go from start and end and find either min or max value (based on ascending or descending what we want).
# - so, in selection sort, in each iteration, we'll only fine the min value.
#
# - iteration 1: min=1  min=1   min=1   min=1                =>  [1,7,3,2]   ;   [1] becomes sorted array, rest [7,3,2] is unsorted array
# - iteration 2: min=7  min=3   min=2           ==sort 2 & 7==>  [2,3,7]     ;   [1,2] becomes sorted array, rest [3,7] is unsorted array
# - iteration 3: min=3  min=3                                =>  [3,7]       ;   [1,2,3] becomes sorted array, rest [7] is unsorted array
#
# - so, we are swapping only once in each iteration.
#
###################################################


# BUBBLE SORT
'''
def bubble_sort(list):
    # for i in range(len(list)-1):
    #     for j in range(len(list)-1-i):
    # OR
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list = [5,3,9,6,7,2]

bubble_sort(list)
print(list)
'''


# SELECTION SORT

def selection_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]
        print(list)

list = [5,3,89,9,6,90,7,2]

selection_sort(list)
print(list)
