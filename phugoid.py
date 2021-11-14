#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 23:51:28 2021

@author: guru
"""

import matplotlib.pyplot as plt
import numpy as np


def vdot(theta,v):
    v_dot=-np.sin(theta)-(D*v**3)
    return v_dot

def thetadot(theta,v):
    theta_dot=(-np.cos(theta)/v)+v
    return theta_dot


v=[]
theta=[]
time=[]

D=0.05
v0=1.0

theta0=5*np.pi/180

dt=0.001
Tp=50
nsteps=int(Tp/dt)

for t in range(nsteps):
    
    vbar=v0+0.5*dt*vdot(theta0,v0)
    thetabar=theta0+0.5*dt*thetadot(theta0,v0)
    vnp1=v0+dt*vdot(thetabar,vbar)
    thetanp1=theta0+dt*thetadot(thetabar,vbar)
    v0=vnp1
    theta0=thetanp1
    v.append(vnp1)
    theta.append(thetanp1*180/(np.pi))
    time.append(t*dt)
    
    

plt.plot(time,theta,'g',label='glide angle')
plt.xlabel('time(s')
plt.ylabel('glide angle(degrees)')
plt.legend()
plt.grid()
plt.show()

plt.plot(time,v,'r',label='velocity')
plt.xlabel('time(s)')
plt.ylabel('velocity(m/s)')
plt.legend()
plt.grid()
plt.show()



plt.xlabel('velocity')
plt.ylabel('glide angle')
plt.grid()
plt.plot(v,theta,'b')
plt.show()
    
    
