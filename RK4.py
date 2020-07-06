# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:20:28 2020

@author: Guru
"""

import numpy as np
import matplotlib.pyplot as plt
import math 
#defining function on RHS
def f(x,y):
    f=x+y
    return f

x=input("enter initial value of x: ")
y=input("enter initial value of y: ")
h=input("enter the step: ")
xp=input("enter value of x at which yis required:")
n=int((xp-x)/h)
for i in range(n):   
    k1=h*f(x,y)
    k2=h*f((x+(h/2)),(y+(k1/2)))
    k3=h*f((x+(h/2)),(y+(k2/2)))
    k4=h*f((x+h),(y+k3))
    x=x+h
    y=y+((1.0/6.0)*(k1+(2*k2)+(2*k3)+k4)
    print(x,y)



