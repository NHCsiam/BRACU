# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:32:58 2020

@author: ASUS
"""

#easy 1

s={}
p=""
while p!="STOP":
    s=[input().split(",")]
    if p=="STOP":
        break
print(s)
for key,value in s.items():
    print (key,value)