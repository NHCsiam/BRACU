# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 02:29:46 2020

@author: ASUS
"""

#medium 4

s=input("Enter: ")

sub_str1='too'
sub_str2='good'

if s.find(sub_str1):
    if s.find(sub_str2):
        print(s.replace("too good", "excellent"))
else:
    print(s)
