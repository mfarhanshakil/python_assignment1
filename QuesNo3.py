# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:55:27 2019

@author: Farhan Shakil
Course: Python Programming Language 
Roll # PY01052
Email: mfarhanshakil@gmail.com
Assignment # 1
Question # 3
Python program to Display CURRENT DATE & TIME
"""

from datetime import datetime                   # Import 'datetime' from Module

date_time = datetime.now()                      # Read Current Date & Time
date_data = date_time.strftime("%d-%B-%Y")      # Save Date as String
day_data  = date_time.strftime("%A")            # Save Day as String
time_data = date_time.strftime("%H:%M:%S")      # Save Time as String

print("\n Date = ", date_data)	                 # Display Date on Screen
print(" Day  = ", day_data)	                    # Dipplay Day on Screen
print(" Time = ", time_data)                   # Display Time on Screen 