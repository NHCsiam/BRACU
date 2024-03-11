# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 01:53:42 2020

@author: ASUS
"""

#easy 2

L=[]
L2=[]

s=int(input("Enter range:"))
for i in range(0,s):
    s=input("Enter: ")
    L.append(s)

s=int(input("Enter another range:"))
for i in range(0,s):
    s2=input("Enter: ")
    L2.append(s2)

L[-1:]=L2

print(L)
