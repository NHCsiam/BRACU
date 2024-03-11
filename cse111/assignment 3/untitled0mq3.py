# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:38:46 2020

@author: ASUS
"""


lst = input().split(",")


name = [] #for storing names
mark = [] #for storing marks
i=0
while i<len(lst):
    if i%2==0:
        name.append(lst[i])
    else:
        mark.append(lst[i])
    i+=1

i = 0 
while i<len(name)-1:
    j = i+1
    minIndex = i 
    while j<len(name):
        if name[j]<name[minIndex]:
            minIndex = j
        j+=1
    temp = name[i]
    name[i] = name[minIndex]
    name[minIndex] = temp
    temp = mark[i]
    mark[i] = mark[minIndex]
    mark[minIndex] = temp
    i+=1
i=0
while i<len(name):
    print(name[i],mark[i],end=",")
    i+=1
print("\b")    