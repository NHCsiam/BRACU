# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 02:48:15 2020

@author: ASUS
"""

#task 1


class Student:
    id=0
    
    def __init__(self,name,department,age,cgpa):
        self.name=name
        self.department=department
        self.age=age
        self.cgpa=cgpa
        Student.id+=1
    def get_details(self):
        print('ID:',Student.id)
        print('Name:',self.name)
        print('Department:',self.department)
        print('Age:',self.age)
        print('CGPA:',self.cgpa)
        
    @classmethod
    def from_String(cls,other):
        name,department,age,cgpa= other.split('-')
        obj = cls (name,department,age,cgpa)
        return obj
    
    
    
s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()    
    
print('Instance variables can be accessed directly by calling the variable name inside the class and Class variables can be accessed by calling with the class name.')
print('Instance methods can access the instance through self where, Class methods need cls to access.')  