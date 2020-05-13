# -*- coding: utf-8 -*-
def sqrt(number=None):
    if number is None:
        return number
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    test=1
    while True:
        if test*test > number:
            return test-1
        test+=1
    pass

print ("Pass" if  (None == sqrt()) else "Fail")  #test without input

print ("Pass" if  (0 == sqrt(0)) else "Fail") #test for value 0

print ("Pass" if  (4 == sqrt(16)) else "Fail") #test for a random value

print ("Pass" if  (1 == sqrt(1)) else "Fail") #test for 1

print ("Pass" if  (15 == sqrt(225)) else "Fail") #test for a large value

