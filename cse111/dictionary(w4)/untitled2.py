# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:20:40 2020

@author: ASUS
"""


    
k=int(input())
lol=int(input())
n=1
i=1
dict={}
while True:
    c=((3 * i^2 )- i)/2
    dict[i]=int((2*i * (2*i- i))/2)
    if dict[i] >k:
        dict.pop(i)
        break
    else:
        i+=1
print(dict)
if True:
    for name in dict:
        if dict[name]==lol:
            print("Key:",name)
            print("Value",lol)
else:      
    print("no such value exist")