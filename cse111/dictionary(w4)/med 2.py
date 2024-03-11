# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 01:08:57 2020

@author: ASUS
"""

#med 2



dict1 = {}
while True:
    s=input()
    if s=="STOP":
        break
    x=int(s)
    if x not in dict1:
        dict1[x] = 1
    else:
        dict1[x] += 1
for key,values in dict1.items():
    print(key,"-",values,"times")