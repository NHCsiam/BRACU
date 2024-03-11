# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:32:58 2020

@author: ASUS
"""

#easy 1

s={}
s1=""
while s!="STOP":
    s=[map(str,input().split())]
    if s=="STOP" :
        break
print(s[0])