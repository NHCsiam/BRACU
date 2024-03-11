# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 17:11:00 2020

@author: ASUS
"""

class Dessert:
     def __init__(self, name):
         self.name = name
         self.type='dessert'

     def review(self):
          print('Dessert Review:', self.name)
          
class Cheesecake(Dessert):
    def __init__(self,name,type1='sweet and dense dessert'):
        super().__init__(name)
        self.type=type1
        
    def review(self):
        super().review()
        print("It is a"+self.type+",enough to improve your mood!")
    
class Red_velvet(Dessert):
    def __init__(self,name):
        super().__init__(name)
        
    def review(self):
        super().review()
        print("It is a "+self.type+" which has an acidic taste from the use of buttermilk and vinegar")


d1 = Cheesecake('Oreo Cheesecake','sweet and dense dessert')
d2 = Red_velvet('Red Velvet cake')
d1.review()
print('=========================')
d2.review()
print('=========================')