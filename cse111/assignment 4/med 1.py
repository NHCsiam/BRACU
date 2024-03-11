# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:52:17 2020

@author: ASUS
"""

#medium 1

L=[]
s=''
while s!="STOP":
    s=input("Enter: ")
    L.append(s)
    if s=="STOP" :
        break
    
L=sorted(L)
del L[len(L)-1]
c=0

while c<len(L):
    c2=0
    c3=1
    while(c2<len(L)):
        if (c==c2):
            pass
        elif (c!=c2):
            if (L[c]==L[c2]):
                c3+=1
                del L[c2]
        c2+=1
    print(L[c],"-",c3,"times")
    c+=1