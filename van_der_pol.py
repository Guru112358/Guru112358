# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def dxdt(x,y):
    dx_dt=mu*(x-((1/3)*(x**3))-y)
    return dx_dt
    
def dydt(x):   
    dy_dt=x
    return dy_dt


X=[]
Y=[]
time=[]
dt=0.001
Tp=40
nsteps=int(Tp/dt)
x0=0.1
y0=0.1
mu=0.8

for t in range(nsteps): 
    
    xbar=x0+0.5*dt*dxdt(x0,y0)
    ybar=y0+0.5*dt*dydt(x0)
    xnp1=x0+dt*dxdt(xbar,ybar)
    ynp1=y0+dt*dydt(xbar) 
    x0=xnp1
    y0=ynp1
    X.append(xnp1)
    Y.append(ynp1)
    time.append(t*dt)

#postprocessing  the results

plt.plot(time,X,'r')
plt.xlabel("time")
plt.ylabel("X")
plt.title("X vs time")
plt.grid()
plt.show()
 
plt.plot(time,Y,'b')
plt.xlabel("time")
plt.ylabel("Y")
plt.title("Y vs time")
plt.grid()
plt.show()

plt.plot(X,Y,'g')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Phase plot")
plt.grid()
plt.show()



