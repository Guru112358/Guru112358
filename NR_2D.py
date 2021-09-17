#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:22:57 2021

@author: guru
"""

#this program solves a system of two non linear equations using the Newton Rapson method

import numpy as np
import matplotlib.pyplot as plt
import math


def f1(x,y):
    func1=y-math.exp(x)
    return func1

def f2(x,y):
    func2=x+y-2
    return func2
    
def Jacobian(f1,f2,x,y,h):
    
    f1x=(f1(x+h,y)-f1(x,y))/h
    f1y=(f1(x,y+h)-f1(x,y))/h
    f2x=(f2(x+h,y)-f2(x,y))/h
    f2y=(f2(x,y+h)-f2(x,y))/h
    J=np.array([f1x,f1y,f2x,f2y]).reshape(2,2)
    
    return J

def NR_routine(x0,y0,f1,f2,niter,alpha,h,epsilon):
    
    res=[]
    count=[]
   
    for i in range(0,niter):
        
        count.append(i)
      
        Jprime=np.linalg.inv(Jacobian(f1,f2,x0,y0,h))
        xnp1=x0-(Jprime[0][0]*f1(x0,y0)+Jprime[0][1]*f2(x0,y0))
        ynp1=y0-(Jprime[1][0]*f1(x0,y0)+Jprime[1][1]*f2(x0,y0))
        
        r=math.sqrt(((x0-xnp1)**2)+((y0-ynp1)**2))
        
        res.append(r)

        
        x0=xnp1
        y0=ynp1
            
        if((r)<epsilon):
            break
        
    plt.xlabel("number of iterations")
    plt.ylabel("Residual")    
    plt.title("Error of Estimate")
    plt.yscale('log')
    #plt.xscale('log') 
    plt.grid()        
    plt.plot(count,res,'r')
    plt.show()
    
    return xnp1,ynp1
            
     
 
      
x,y = NR_routine(0.1,0.1,f1,f2,25,0.5,0.00000001,0.000000001)


print("The roots of the system of non linear equations are: ")
print()
print("x -->",x)
print("y -->",y)
    
    