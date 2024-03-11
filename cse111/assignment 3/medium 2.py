# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 03:44:44 2020

@author: ASUS
"""

#medium 2

s=input("Enter: ")

if s.isalpha() :
    print("WORD")
elif s.isnumeric:
    print("NUMBER")
else:
    print("MIXED")
