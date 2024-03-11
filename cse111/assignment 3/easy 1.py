# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 19:59:41 2020

@author: ASUS
"""

#easy 1

vowels=("a","e", "i", "o", "u", "A", "E","I","O","U")

msg=input("enter msg: ")
n_msg=""
count=0

for i in msg:
    if i not in vowels:
        n_msg+=i
for num_msg in msg:
    if num_msg in vowels:
        count+=1
        
print(n_msg,count)