# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 14:52:52 2020

@author: ASUS
""" 
#task 2

class Flower:          
    def __init__(self):
        pass


flower1 =Flower();
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print('=====================')
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)

if flower1==flower2:
    print('they are same')
else:
    print('they are different')
