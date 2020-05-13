# -*- coding: utf-8 -*-
def get_min_max(ints=[]):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints)==0:
        return None,None
    large=ints[0]
    small=ints[0]
    for i in range(1,len(ints)-1,2):
        if ints[i] < ints[i+1]:
            
            if ints[i] < small:
                small=ints[i]
                
            if ints[i+1] > large:
                large = ints[i+1]
        else:
            
            if ints[i+1] < small:
                small=ints[i+1]
                
            if ints[i] > large:
                large=ints[i]   
    return small,large
    pass

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 11)]  # a list containing 0 - 9
random.shuffle(l)


print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print ("Pass" if ((0, 10) == get_min_max(l)) else "Fail")
l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")
