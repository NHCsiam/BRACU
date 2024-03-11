# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 16:29:27 2020

@author: ASUS
"""

#hard 2

word=input("Enter word: ")
reverse=word[::-1]
s=""
st=""
string=""
for i in range(0,len(word)):
    s=s+word[i]
    st=st+reverse[i]
    if s==st[::-1]:
        string=s
        break
length=len(string)
leng=len(word)
mid=word[length:leng-length]
if string in mid:
    print(string)
else:
    print("Not Palindrome Substring")