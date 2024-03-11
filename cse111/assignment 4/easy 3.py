# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 13:37:53 2020

@author: ASUS
"""

#easy 3

L=[]

for i in range(0,10):
    s=input("Enter: ")
    if s in L:
        p=input("Enter another number: ")
    if s in L:
        p=input("Enter another number: ")    
        L.append(p)
    else:
        L.append(s)
print(L)
