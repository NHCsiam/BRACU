# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 23:59:36 2020

@author: ASUS
"""

#med 4

s=input("enput: ").split(',')
dic1={}
for i in s:
    lo=i.split(':')
    dic1[lo[0]]=int(lo[1])

s=input("enput: ").split(',')
dic2={}
for i in s:
    lo=i.split(':')
    dic2[lo[0]]=int(lo[1])
    
for key,val in dic2.items():
    if key in dic1.keys():
        dic1[key] += dic2[key]
    else:
        dic1[key]=val
    
print(dic1)

list_value=[]
ulist_value=[]

for key in dic1.keys():
    list_value.append(dic1[key])
    
for i in list_value:
    if i not in ulist_value:
        ulist_value.append(i)
        
ulist_value=tuple(ulist_value)        
        
print("value: ",ulist_value)