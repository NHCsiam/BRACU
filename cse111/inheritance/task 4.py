# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 05:25:21 2020

@author: ASUS
"""

#task 4

class Account:
    def __init__(self,balance):
        self._balance = balance
 
    def getBalance(self):
        return self._balance
    
class CheckingAccount(Account):
    
    numberOfAccount=''
    numberOfAccount=str(0)
    
    def __init__(self,balance=0):
        super().__init__(float(balance))
        CheckingAccount.numberOfAccount=int(CheckingAccount.numberOfAccount)+1
        CheckingAccount.numberofAccount=CheckingAccount.numberOfAccount
        CheckingAccount.numberOfAccount=str(CheckingAccount.numberofAccount)
        
    def __str__(self):
        
        return 'Account Balance: ' + str(super().getBalance())
    
        
print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)
print(CheckingAccount())
print(CheckingAccount(100.00))
print(CheckingAccount(200.00))
print('Number of Checking Accounts: '+CheckingAccount.numberOfAccount)        
     
