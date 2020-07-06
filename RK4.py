# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 22:32:05 2020

@author: Guru
"""
import numpy as np
import matplotlib.pyplot as plt
import math 


#simple program to solve ODE by Runge Kutta 4th order method
#creating a function to do the numerical tasks
def RK4(x0,y0,xp,h):
    x=[]
    y=[]
    n=(xp-x0)/h
    for i in range(int(n)):
        k1=h*f(x0,y0)
        x2=x0+h/2
        y2=y0+k1/2
        k2=h*f(x2,y2)
        x3=x0+h/2
        y3=y0+(k2/2)
        k3=h*f(x3,y3)
        x4=x0+h
        y4=y0+k3
        k4=h*f(x4,y4)
        x0=(x0+h)
        y0=(y0+(1.0/6.0)*(k1+2*k2+2*k3+k4))
        x.append(x0)
        y.append(y0)
        print(x,y)
        plt.plot(x,y)

def f(x,y):
    f=(5*x**2-y)/(np.exp(x+y))
    return f


print(RK4(0,1,10,0.1))
