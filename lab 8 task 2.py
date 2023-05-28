# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:18:45 2022

@author: ebaa
"""
print ("lab 8 task 2")
def square(a):
    l = len(a)
    i=0
    while (i<l):
        print (a[i]*a[i])
        i+=1    
a=eval(input("Enter list(a): "))
square (a)

    