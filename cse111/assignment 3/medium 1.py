# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 03:11:29 2020

@author: ASUS
"""

#medium 1

s=input("ENTER: ")
upper_case=0
lower_case=0


for i in s:
      if(i.islower()):
            lower_case+=1
      elif(i.isupper()):
            upper_case+=1
    
if lower_case > upper_case:
    temp=s.lower()
    print(temp)
else:
    temp=s.upper()
    print(temp)
        
        

