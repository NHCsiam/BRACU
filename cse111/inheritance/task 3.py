# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 19:47:15 2020

@author: ASUS
"""

#task 3
 
class RealNumber:

     def __init__(self, r=0):
         self.__realValue = r
     def getRealValue(self):
        return self.__realValue
     def setRealValue(self, r):
        self.__realValue = r
     def ping(self):
        print('I am in RealNumber class')
     def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

class  ComplexNumber(RealNumber):
    
    def __init__(self,r=1,i=1):
        super().__init__(float(r))
        self.__i=float(i)
        
    def setimaginaryvalue(self, i):
        self.__i=i
    
    def getimaginaryvalue(self):
        return self.__i
        
    def __str__(self):
        return super().__str__()+"\n"+'ImaginaryPart: '+str(self.getimaginaryvalue())
        
    
    
cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)
print('---------')       