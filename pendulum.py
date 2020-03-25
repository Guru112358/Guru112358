# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:21:17 2020

@author: Guru
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import*
#governing equation is a second order ODE   thetadoubledot=-(mu*thetadot)-(g/l)*sin(theta)
#note:small angle approximation is NOT followed
#initial parameters
g=9.81 
l=1 #length of the pendulum
mu=0.5 #generalised damping term
theta0=np.pi/4 #initial angular displacement in radians
thetadot0=0.0 #initial velocity
dt=0.01 #time step
#creating some lists for appending data
x1=[]
x2=[]
x3=[]
x4=[]
#creating a function to return angular acceleration
def thetadoubledot(thetadot,theta):
    thetadoubledot=-(mu*thetadot)-(g/l)*np.sin(theta)
    return thetadoubledot
#creating a function to do time stepping and solve the differential equation
#a simple Euler time stepping scheme is used
#disclaimer:this scheme is only first order accurate and only serves as a simple numerical demonstration for a common physics problem,ie the simple pendulum
#larger time steps and longer running time(t) will cause numerical error to build up quickly.
def theta(t):
    theta=theta0
    thetadot=thetadot0
    for t in np.arange(0,t,dt):
       
        x1.append(t)
        thetadoubledot1=thetadoubledot(thetadot,theta)
        theta+=thetadot*dt#time stepping to obtain displacement
        thetadot+=thetadoubledot1*dt #time stepping to obtain angular velocity
        x2.append(theta*180/(np.pi))
        x3.append(thetadot)
        x4.append(theta)
          
    return theta,thetadot
#creating a function for post processing
def main():
    
    t=10
    theta(t)
    subplot(2,1,1)
    title('angular displacement vs time')
    ylabel('angular displacement(degrees)')
    xlabel('time(seconds)')
    plot(x1,x2)
    show()
    
    subplot(2,1,2)
    title('phase plot')
    xlabel('angular displacement(rad)')
    ylabel('angular velocity(rad/s)')
    plot(x4,x3)
    show()
#calling the manin function
main()
