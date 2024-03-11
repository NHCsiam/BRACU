# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 02:27:37 2020

@author: ASUS
"""

#task 6

class Fruit:
     def __init__(self, formalin=False, name=''):
         self.__formalin = formalin
         self.name = name
    
     def getName(self):
         return self.name
    
     def hasFormalin(self):
         return self.__formalin

class testFruit:
     def test(self, f):
         print('----Printing Detail----')
         if f.hasFormalin():
             print('Do not eat the',f.getName(),'.')
             print(f)
         else:
             print('Eat the',f.getName(),'.')
             print(f)

class Mango(Fruit,testFruit):
    def __init__(self,formalin=True,name='Mango'):
        super().__init__(formalin,name)
    
    def __str__(self):
        return super().getName()+'s are bad for you'
    
class Jackfruit(Fruit,testFruit):
    def __init__(self, formalin=False, name='Jackfruit'):
        super().__init__(formalin,name)
    
    def __str__(self):
        return super().getName()+'s are good for you'

m = Mango()
j = Jackfruit()
t1 = testFruit()
t1.test(m)
t1.test(j)

