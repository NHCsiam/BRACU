# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 16:15:39 2020

@author: ASUS
"""


class Harry_Potter:
    book_count=0
    def __init__(self,name,year):
        self.name=name
        self.year=year
        Harry_Potter.book_count+=1
        
    def set_name(self,name):
        self.name=name
    def set_year(self,year):
        self.year=year
        
    def display_book_info(self):
        dis="Book-->"+str(self.year)+':'+str(self.name)
        return dis
        
        
print("Book Count:", Harry_Potter.book_count)
print("=======================")
b1 = Harry_Potter("Harry Potter and the Philosopher's Stone.",1997)
print(b1.display_book_info())
b2 = Harry_Potter("Harry Potter and the Chamber of Secrets.", 0)
b2.set_year(1998)
print(b2.display_book_info())
b3 = Harry_Potter("Harry Potter and the Prisoner of Azkaban.",1999)
print(b3.display_book_info())
b4 = Harry_Potter("Default", 0)
b4.set_name("Harry Potter and the Goblet of Fire.")
b4.set_year(2000)
print(b4.display_book_info())
print("=======================")
print("Book Count:", Harry_Potter.book_count)        
        
        