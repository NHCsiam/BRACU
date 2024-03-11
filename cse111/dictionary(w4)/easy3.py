# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 22:50:45 2020

@author: ASUS
"""

#task 3



dict={}
i=0
while i<10:
    v=input()
    k=i
    if v not in dict.values():
        dict[i]=v
    
    else:
        print("enter another value")
        
        i=i-1
    i+=1
    
print(dict)




