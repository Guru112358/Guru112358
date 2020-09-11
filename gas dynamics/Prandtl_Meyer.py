

import math

#defining Prandtl  Meyer Expansion function that returns a value in degrees
#this function calculates the value of the Prandtl Meyer expansion dunction for a given upstream Mach number



def prandtl_meyer(M):
    gamma=1.40
    nu_rad=math.sqrt((gamma+1)/(gamma-1))*math.atan((((gamma-1)/(gamma+1))*((M*2)-1)))-math.atan(math.sqrt((M**2)-1))
    nu_deg=nu_rad*((180.0)/(math.pi))  
    return nu_deg

#This function inverts the above function numerically to give a value of the downstream mach number

def prandtl_meyer_inverse(nu2):    
    nuinf=(math.pi/2)*((math.sqrt(6))-1)   
    A =1.3604
    B =0.0962
    C =-0.5127
    D =-0.6722
    E =-0.3278
    y=(nu2/nuinf)**(2.0/3.0)
    M2=(1+(A*y)+(B*y**2)+(C*(y**3)))/(1+(D*y)+(E*y**2))       
    return M2


   #This function calls the above two function to compute the downstream Mach number when upstream mach number is known along with deflection angle 
def Prandtl_Meyer_solve():   
    M1=float(input("Enter the upstream Mach number:-"))
    theta=float(input("enter the flow deflection corner angle(degrees):-"))
    nu2=prandtl_meyer(M1)+theta
    M2=prandtl_meyer_inverse(nu2)
    print("The Downstream mach number is: ",M2)
     
#calling the solution function   

Prandtl_Meyer_solve()
