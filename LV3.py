#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 19:54:44 2020

@author: guru
"""

import matplotlib.pyplot as plt


def dx_dt(x,y):
    dxdt=(alpha*x)-(beta*x*y)
    return dxdt

def dy_dt(x,y,z):
    dydt=(delta*x*y)-(e*y*z)-(gamma*y)
    return dydt


def dz_dt(y,z):
    dzdt=(-f*z)+(g*y*z)
    return dzdt
    
X=[]
Y=[]
Z=[]
time=[]

alpha=1.0
beta=1.0
gamma=1.0
delta=1.0
e=1.0
f=1.0
g=1.0
dt=0.001
Tp=25
nsteps=int(Tp/dt)

x0=0.5
y0=0.5
z0=0.5

for t in range(nsteps):
    
    xbar=x0+dt*dx_dt(x0,y0)
    ybar=y0+dt*dy_dt(x0,y0,z0)
    zbar=z0+dt*dz_dt(y0,z0)
    
    xnp1=x0+0.5*dt*(dx_dt(xbar,ybar)+dx_dt(x0,y0))
    ynp1=y0+0.5*dt*(dy_dt(xbar,ybar,zbar)+dy_dt(x0,y0,z0))
    znp1=z0+0.5*dt*(dz_dt(ybar,zbar) +dz_dt(y0,z0))
    
    x0=xnp1
    y0=ynp1
    z0=znp1
    X.append(xnp1)
    Y.append(ynp1)
    Z.append(znp1)
    time.append(t*dt)
    

plt.plot(time,X,'r',label='Prey')
plt.xlabel("Time")
plt.ylabel("Population")
plt.plot(time,Y,'g',label='Middle Predator')
plt.plot(time,Z,'b',label='Apex Predator')
plt.legend()
plt.grid()
plt.show()

plt.xlabel('Prey population')
plt.ylabel(' Middle Predator population')
plt.grid()
plt.plot(X,Y,'g')
plt.show()

plt.xlabel('Prey population')
plt.ylabel(' Apex Predator population')
plt.grid()
plt.plot(X,Z,'r')
plt.show()


ax = plt.axes(projection='3d')
ax.set_xlabel('Prey')
ax.set_ylabel('middle predator ')
ax.set_zlabel('Apex predator')
plt.tight_layout()
ax.plot3D(X,Y,Z ,'blue')
plt.show()