# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:29:33 2019

@author: Farhan Shakil
Course: Python Programming Language 
Roll # PY01052
Email: mfarhanshakil@gmail.com
Assignment # 1
Question # 5
Python Program which Accepts the User's First and Last Name
It then Print Them in Reverse Order with Space Between Them
"""
 
first_name = input("Input Your First Name ===> ")   # Read First Name
last_name  = input("Input Your Last Name  ===> ")   # REad Last Name

print ("\n\t" + last_name + " " + first_name)       # Display Name in Reverse
print ("\n\t" + last_name[::-1] + " " + first_name[::-1])