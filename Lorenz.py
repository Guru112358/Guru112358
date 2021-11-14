#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 10:27:51 2020

@author: aero
"""
import matplotlib.pyplot as plt

#References :-Non Linear dynamics and  Chaos by Strogatz (duh)
# https://mathworld.wolfram.com/LorenzAttractor.html
# sigma -Prandtl number
# rho= Ra/Rac
#beta =4/(1+a^2)  geometric factor

def dxdt(x,y):
    dx_dt=sigma*(y-x)
    return dx_dt

def dydt(x,y,z):
    dy_dt=(x*(rho-z))-y
    return dy_dt

def dzdt(x,y,z):
    dz_dt=(x*y)-(beta*z)
    return dz_dt


sigma=10.0
beta=8/3
rho=28
    
X=[]
Y=[]
Z=[]
time=[]
dt=0.0001
Tp=50
nsteps=int(Tp/dt)
x0=0.01
y0=0.0
z0=0.0

for t in range(nsteps): 
    
    k1=dxdt(x0,y0)
    l1=dydt(x0,y0,z0)
    m1=dzdt(x0,y0,z0)

    k2=dxdt(x0+0.5*k1*dt,y0+0.5*l1*dt)
    l2=dydt(x0+0.5*k1*dt,y0+0.5*l1*dt,z0+0.5*m1*dt)
    m2=dzdt(x0+0.5*k1*dt,y0+0.5*l1*dt,z0+0.5*m1*dt)

    k3=dxdt(x0+0.5*k2*dt,y0+0.5*l2*dt)
    l3=dydt(x0+0.5*k2*dt,y0+0.5*l2*dt,z0+0.5*m2*dt)
    m3=dzdt(x0+0.5*k2*dt,y0+0.5*l2*dt,z0+0.5*m2*dt)

    k4=dxdt(x0+k3*dt,y0+l3*dt)
    l4=dydt(x0+k3*dt,y0+l3*dt,z0+m3*dt)
    m4=dzdt(x0+k3*dt,y0+k3*dt,z0+m3*dt)

    xnp1=x0+(dt/6)*(k1+(2*k2)+(2*k3)+k4)
    ynp1=y0+(dt/6)*(l1+(2*l2)+(2*l3)+l4)
    znp1=z0+(dt/6)*(m1+(2*m2)+(2*m3)+m4)

    x0=xnp1
    y0=ynp1
    z0=znp1
    
    X.append(xnp1)
    Y.append(ynp1)
    Z.append(znp1)
    time.append(t*dt)
    

#postprocessing  the results
plt.plot(X,Z,'r')
plt.xlabel("x")
plt.ylabel("z")
plt.grid()
plt.show()

ax = plt.axes(projection='3d')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.tight_layout()
ax.plot3D(X,Y,Z ,'m')
plt.show()

plt.plot(time,X,'r')
plt.xlabel("time")
plt.ylabel("X")
plt.grid()
plt.show()
 
plt.plot(time,Y,'b')
plt.xlabel("time")
plt.ylabel("Y")
plt.grid()
plt.show()

plt.plot(time,Z,'g')
plt.xlabel("time")
plt.ylabel("Z")
plt.grid()
plt.show()

