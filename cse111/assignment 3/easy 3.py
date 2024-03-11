# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:22:08 2020

@author: ASUS
"""

#easy 3 

vowels=("a","e", "i", "o", "u")
s=input("Enter: ")
length=len(s)

if length>1:
  
        if s[-1:] in vowels :            
             print('yay'+s)
        else:            
            s = s[-1:] + s[:-1]
            print(s+'ay')
else:
    print(s)
           