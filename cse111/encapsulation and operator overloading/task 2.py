# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 04:01:21 2020

@author: ASUS
"""

#task 2

class Teacher:
    
    def __init__(self,name,department):
        self.__name=name
        self.__department=department
        self.__course=[]
    def printDetail(self):
         print('====================================')
         print('Name:',self.__name)
         print('Department:', self.__department)
         print('List of courses')
         print('====================================')
         for i in self.__course:
             print(i)
         print('====================================')
            
            
    def addCourse(self,c_code):
        self.__course.append(c_code.c_name)
         
        
class Course:
    def __init__(self,c_name):
        self.c_name=c_name
        
            
t1 = Teacher("Saad Abdullah", "CSE")
t2 = Teacher("Mumit Khan", "CSE")
t3 = Teacher("Sadia Kazi", "CSE")
c1 = Course("CSE 110 Programming Language I")
c2 = Course("CSE 111 Programming Language-II")
c3 = Course("CSE 220 Data Structures")
c4 = Course("CSE 221 Algorithms")
c5 = Course("CCSE 230 Discrete Mathematics")
c6 = Course("CSE 310 Object Oriented Programming")
c7 = Course("CSE 320 Data Communications")
c8 = Course("CSE 340 Computer Architecture")
t1.addCourse(c1);
t1.addCourse(c2);
t2.addCourse(c3);
t2.addCourse(c4);
t2.addCourse(c5);
t3.addCourse(c6);
t3.addCourse(c7);
t3.addCourse(c8);
t1.printDetail();
t2.printDetail();
t3.printDetail();