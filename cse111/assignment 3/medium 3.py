# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 18:53:00 2020

@author: ASUS
"""

#medium 3

s=input("Enter: ")

count1=0
count2=0

for i in s:
    if i.isupper():
        a=s.index(i)
        break    
for i in s:
    if i.isupper():
        count2=count2 + s.index(i)
        c=count2-a
s=s[(count1+3):c]
if s=="":
    print("Blank")
else:
    print(s)
