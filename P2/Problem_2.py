# -*- coding: utf-8 -*-
def Search(array,start,finish,value):
    mid=start+(finish-start)//2
    if start > finish:
        return -1
    if value == array[mid]:
        return mid
    elif array[start] <= array[mid]:
        if value >= array[start] and value < array[mid]:
            return Search(array,start,mid-1,value)
        else:
            return Search(array,mid+1,finish,value)
    else:
        if value > array[mid] and value <= array[finish]:
            return Search(array,mid+1,finish,value)
        else:
            return Search(array,start,mid-1,value)
        
        
def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == Search(input_list,0,len(input_list)-1, number):
        print("Pass")
    else:
        print("Fail")
        

test_function([[], 6])  #test for empty array

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])  #test for first element in array

test_function([[1, 2,3,4,5,6,7,8,9,12], 12]) #test for last element in unrotated array

test_function([[6, 7, 8, 1, 2, 3, 4], 4])   #test for last element in rotated array

test_function([[6, 7, 8, 1, 2, 3, 4], 10])  #test for a element not in array