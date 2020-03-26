from random import random
import matplotlib.pyplot as plt
import math
#this program computes the value of Pi approximately by employing a Monte carlo method
#the random() module is called to produce random points between 0 and 1 in x and y coordinates of a square region of space 1 X 1.
#if they fall within a unit circle,the point is counted.
#increasing number of random points increases accuracy.
#this method is limted by the quality of the pseudorandom number generator and number of points the memory can handle.
n=10000
count=0
for i in range(1,int(n)):
    #calling random numbers between 0 and 1 using the random() function from the random library
    x=random()
    y=random()
    r=math.sqrt(x**2+y**2) #computing radius of the circle
    if(r<=1):
        count+=1 #incrementing each time the random point falls within the circle
        Pi=(4*(count/i))
        plt.scatter(x,y) #plotting the points that fall within the circle
print(Pi)  
      
