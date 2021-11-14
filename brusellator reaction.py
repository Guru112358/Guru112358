#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:55:09 2020

@author: guru
"""

import matplotlib.pyplot as plt


def dxdt(x,y):
    dx_dt=a+((x**2)*y)-(b*x)-x
    return dx_dt

def dydt(x,y):
    dy_dt=(b*x)-((x**2)*y)
    return dy_dt

a=1
b=4
X=[]
Y=[]
time=[]
dt=0.001
Tp=50
nsteps=int(Tp/dt)
x0=0.01
y0=0.01


for t in range(nsteps):
    
    xbar=x0+0.5*dt*dxdt(x0,y0)
    ybar=y0+0.5*dt*dydt(x0,y0)
    
    xnp1=x0+dt*dxdt(xbar,ybar)
    ynp1=y0+dt*dydt(xbar,ybar)
    
    x0=xnp1
    y0=ynp1
    X.append(xnp1)
    Y.append(ynp1)
    time.append(t*dt)

#postprocessing  the results


plt.xlabel("Time")
plt.ylabel("Concentration")
plt.plot(time,X,'r',label='X')
plt.plot(time,Y,'b',label='Y')
plt.legend()
plt.grid()
plt.show()


plt.plot(X,Y,'g')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Phase plot")
plt.grid()
plt.show()

