# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:15:51 2019

@author: Farhan Shakil
Course: Python Programming Language 
Roll # PY01052
Email: mfarhanshakil@gmail.com
Assignment # 1
Question # 4
Python Program to Calculate Area of a circle using Radius Input
"""

from math import pi                     # Import Value of PI from Math Module
                                        # Read Value of Radius from User
radius_data = float(input ("Enter Radius of Circle ===> "))
area_data   = pi * radius_data**2       # Calculate & Save Area of Circle
                                        # Diplay Radius, PI & Area on Screen
print ("\n\t Radius of Circle = " , radius_data)
print ("\t Value of PI      = " , pi)
print ("\t Area of Circle   = " , area_data)