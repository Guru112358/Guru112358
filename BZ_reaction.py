#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 23:53:43 2020

@author: guru
"""

import matplotlib.pyplot as plt


def dxdt(x,y):
    dx_dt=a-x-((4*x*y)/(1+x**2))
    return dx_dt

def dydt(x,y):
    dy_dt=(b*x)*(1-(y/(1+x**2)))
    return dy_dt

a=10
b=2
    
X=[]
Y=[]
time=[]
dt=0.001
Tp=25
nsteps=int(Tp/dt)
x0=1.0
y0=1.0


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

plt.plot(time,X,'r')
plt.xlabel("time")
plt.ylabel("X")
plt.title("reactant X vs time")
plt.grid()
plt.show()
 
plt.plot(time,Y,'b')
plt.xlabel("time")
plt.ylabel("Y")
plt.title("reactant Y vs time")
plt.grid()
plt.show()

plt.plot(X,Y,'g')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Phase plot")
plt.grid()
plt.show()

