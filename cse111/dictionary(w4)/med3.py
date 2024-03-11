# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 02:59:15 2020

@author: ASUS
"""



s=input("enput: ").split(',')
dic1={}
for i in s:
    lo=i.split(':')
    dic1[lo[0]]=(lo[1])

list=[]
final={}
for i in dic1:
    if dic1[i] not in list:
        list.append(dic1[i])
for i in list:
    elist=[]
    for j in dic1:
        if dic1[j]==i:
            elist.append(j)
    final[i]=elist
print(final)

