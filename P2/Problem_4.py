# -*- coding: utf-8 -*-
def sort_012(arr):
    srt=0
    mid=0
    end=len(arr)-1
    
    while mid <= end:
        if arr[mid]==0:
            arr[mid]+=arr[srt]
            arr[srt]=arr[mid]-arr[srt]
            arr[mid]-=arr[srt]
            srt+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            if mid == end:
                end-=1
                continue
            arr[mid]+=arr[end]
            arr[end]=arr[mid]-arr[end]
            arr[mid]-=arr[end]
            end-=1

def test_function(test_case):
    sort_012(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0,2]) #testing without a number

test_function([2,2,2,1,1,1,0,0,0]) #testing with an reversely sorted array

test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #tseting with a random array

test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) #testing with a sorted array