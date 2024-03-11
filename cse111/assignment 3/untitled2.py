# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:49:55 2020

@author: ASUS
"""

binary = ''
x = int(input("enter a anumber: "))
count = 1
while x>0:
    rem = x%2
    binary = str(rem) + binary
    x = x//2
    count+=1
ditcount = 0
for i in range(0,count-1,1):
    if binary[i]=='1':
        ditcount+=1
op = 0
i = 1
add = 1
while i<=ditcount:
    op = op + add
    i+=1
    add=add*2
print(op)
#enter a anumber: 37
