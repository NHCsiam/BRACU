# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:32:18 2020

@author: ASUS
"""

#task 3

class Dates():
    
    def __init__(self,date):
        self.date=date
        
    def getDate(self):
        return self.date
        
        
    @classmethod
    
    def toDashDate(cls,other):
        date=other.replace('/','-')
        obj= cls(date)
        return obj
    
    
    
date1 = Dates("05-09-2020")
dateFromDB = "05/09/2020"
date2= Dates.toDashDate(dateFromDB)
if(date1.getDate() == date2.getDate()):
    print("Equal")
else:
    print("Unequa")
    
print('As we replaced date2 "/" with "-" and date1 has "/", also both of the dates numbers are the same that is why the output is Equal.')