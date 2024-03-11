# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 02:57:45 2020

@author: ASUS
"""

#hard 1

s1=input("Enter: ")
s2=input("Enter: ")

str1=""
str2=""

for i in s1:
    if i in s2:
        str1+=i
for i in s2:
    if i in s1:
        str2+=i

if str1=="" and str2=="":
    print('Nothing in common')
elif str1 or str2!="":
    print(str1+str2)
    