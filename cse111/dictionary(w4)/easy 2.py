# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 19:15:03 2020

@author: ASUS
"""

#task 2

s=input("enput: ").split(',')
dic={}
loc=()
for i in s:
    lo=i.split(':')
    dic[lo[0]]=int(lo[1])
    
for i in dic:
    min=dic[i]
    loc=i
    break
for i in dic:
    if min>dic[i]:
        min=dic[i]
        loc=i
print("Minimum: "+loc)
for i in dic:
    max=dic[i]
    loc=i
    break
for i in dic:
    if max<dic[i]:
        max=dic[i]
        loc=i
print("Maximum: "+loc)

    


