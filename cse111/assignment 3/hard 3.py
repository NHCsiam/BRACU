# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:07:39 2020

@author: ASUS
"""

#hard 3

s=input("Enter the passsword: ")
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABETS = ASCII_LOWERCASE + ASCII_UPPERCASE

up_count=0
lo_count=0
sp_count=0
num_count=0
err=0
blist=[]


for i in s:
    if i in ALPHABETS:
        if i>="A" and i<="Z":
            up_count+=1
        if i>="a" and i<="z":
            lo_count+=1
    elif i>="0" and i<="9":
        num_count+=1
    elif i=="_"or i=="$" or i=="#" or i=="@":
        sp_count+=1
if up_count==0:
    blist.append("Uppercase character missing")
    err+=1
if lo_count==0:
    blist.append("Lowercase character missing")
    err += 1
if num_count==0:
    err += 1
    blist.append("Digit Missing")
if sp_count==0:
    blist.append("Special character Missing")
    err += 1
if err==0:
    print("OK")
else:
    p=blist
    b=', '.join(p)
    print(str(b)+"",end=" ")
    
    
    
    
    
    
    
    