# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:34:37 2020

@author: ASUS
"""
#task 1

class DataType:
    def __init__(self,name,value):
        self.name=name
        self.value=value
        
        
data_type1 = DataType('Integer', 1234)
print(data_type1.name)
print(data_type1.value)
print('=====================')
data_type2 = DataType('String', 'Hello')
print(data_type2.name)
print(data_type2.value)
print('=====================')
data_type3 = DataType('Float', 4.0)
print(data_type3.name)
print(data_type3.value)

