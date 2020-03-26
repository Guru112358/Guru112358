# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:41:22 2019

@author: Guru
"""
#This program computes the value of an intgral by using the Monte Carlo method
#any integral can be be broken up into a summation with infinite terms as the step tends to zero according to the fundamental theorem of Integral calculus.
#the function in the integral sign is repeatedly calculated for a series of random points within thr range of the limits.
#this is achieved using the uniform() function  in the random library,it creates random floating point numbers within the specified range.
#for thsi particular example, integral(sin(x)) between 0 and pi is taken as a benchmark.
#a-lower limit
#b-upper limit
import random
import math
n=10000
a=0
b=math.pi
x=[]
y=[]
for i in range(0,int(n)):
     x_=random.uniform(a,b) #creating  random numbers within the limits of integration
     x__=x.append(x_)
     y_=math.sin(x[i])
     y__=y.append(y_)
     
s=sum(y) #computing the sum of the list containing the function values
av=sum(y)/n #computing the average value of the function
I=av*(b-a) #applying fundamental theorem of calculus
print(I)
             
     
     
     
    
    
            
