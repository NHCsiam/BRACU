# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:34:54 2020

@author: ASUS
"""

#task 5

class Dolls:
    Doll='Doll'
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
    def detail(self):
        
        return('{}: {} \nTotal price: {} taka'.format(Dolls.Doll,self.name,self.price))
        
    def __gt__(self,other):
        if self.price>other.price:
            return True
        else:
            return False
        
    def __add__(self,other):
        n=(self.name+' '+other.name)
        p=(self.price+other.price)
        Dolls.Doll+='s'
        return Dolls(n,p)
        



obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thankyou!")

print("=========================")
obj_5=(obj_2+obj_3)
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")

