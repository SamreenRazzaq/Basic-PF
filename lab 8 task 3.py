# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:35:23 2022

@author: ebaa
"""
print("lab 8 task 3")
def count_13(n):
    number = 987654321
    result = []
    for a in str(n):
	     result.append(int(a))
    print(result)
    l=len(result)
    i=0
    one=0
    three=0
    while (i<l):
        if (1==result[i]):
            one+=1
        if (3==result[i]):
            three+=1
        
        i+=1
    tuple = (one,three)
    print (tuple)
n= (input("enter any integer "))
count_13(n)


