#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:43:01 2021

"""
import numpy as np
import matplotlib.pyplot as plt


nx=500
M1=np.linspace(1,25,nx)
M2=np.zeros(nx)
R=287.0
Cp=1005
gamma=1.40
gamma_1=gamma-1
gamma_plus_1=gamma+1

rho1=np.linspace(1.225,8,nx)
rho2=np.zeros(nx)
rho12=np.zeros(nx)
p12=np.zeros(nx)
T12=np.zeros(nx)
deltaS=np.zeros(nx)
po2_po1=np.zeros(nx)


#implementing normal shock relations

M2=np.sqrt((1+(gamma_1/2)*(M1**2))/((gamma*(M1**2))-(gamma_1/2))) #downstream mach number
rho12=(gamma_plus_1*(M1**2))/(2+gamma_1*(M1**2))    #density ration pre and post shock
p12=1+(2*gamma)/(gamma_plus_1)*(M1**2-1)            #static pressure ratio pre and post shock
T12=(1/rho12)*p12                                   #static temperature ratio pre and post shock
deltaS=Cp*(np.log(T12))-R*np.log(p12)               #entropy change [re and post shock
po2_po1=np.exp(-deltaS/R)                           #stagnation pressure ratio
   
#plotting normal shock properties
plt.ylim(0,7)
plt.xlabel("Upstream Mach number")
plt.plot(M1,rho12,'b-',label="Density ratio")
plt.plot(M1,M2,'r-',label="Downstream Mach number")
plt.plot(M1,p12,'g-',label="Static Pressure ratio")
plt.plot(M1,T12,'m-',label="Static Temperature ratio")
plt.plot(M1,po2_po1,label="Stagnation Pressure ratio")

plt.legend()
plt.grid()
plt.show()
