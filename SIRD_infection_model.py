import matplotlib.pyplot as plt

#SIRD model
#S -susceptible population
#I -Infected population
#R -Recovered population
#D -Deceased population

""" These models dont work,never have,and never will represnt the complexities
 of real world epidemics but they are fun to play with """
 
 
def dS_dt(beta,I,S,N):
    dsdt=(-(beta*I*S)/N)
    return dsdt

def dI_dt(beta,I,S,N,gamma,mu):
    dIdt=((beta*I*S)/N)-(gamma*I)-(mu*I)
    return dIdt

def dR_dt(I,gamma):
    return gamma*I

def dD_dt(I,mu):
    return mu*I



gamma=0.035 #recovery rate
mu=0.005  #mortality rate
beta=0.4   #rate of infection

Tp=150
dt=0.001

nsteps=int(Tp/dt)

s0=990
I0=10
R0=0
D0=0
N=1000

S=[]
I=[]
R=[]
D=[]
time=[]

for i in range(nsteps):
    Sbar=s0+dt*dS_dt(beta,I0,s0,N)
    Ibar=I0+dt*dI_dt(beta,I0,s0,N,gamma,mu)
    Rbar=R0+dt*dR_dt(I0, gamma)
    Dbar=D0+dt*dD_dt(I0, mu)
    
    Snp1=s0+0.5*dt*(dS_dt(beta,Ibar,Sbar,N)+dS_dt(beta,I0,s0,N))
    Inp1=I0+0.5*dt*(dI_dt(beta,Ibar,Sbar,N,gamma,mu)+dI_dt(beta,I0,s0,N,gamma,mu))
    Rnp1=R0+0.5*dt*(dR_dt(Ibar, gamma)+dR_dt(I0, gamma))
    Dnp1=D0+0.5*dt*(dD_dt(Ibar, mu)+dD_dt(I0, mu))
    
    s0=Snp1
    R0=Rnp1
    I0=Inp1
    D0=Dnp1
    
    S.append(Snp1)
    I.append(Inp1)
    R.append(Rnp1)
    D.append(Dnp1)
    time.append(i*dt)
    

plt.xlabel("time")
plt.ylabel("Population")
plt.title("SIRD infection model" )
plt.plot(time,S,'b',label='Susceptible')
plt.plot(time,I,'m',label='Infected')
plt.plot(time,R,'lime',label='Recovered')
plt.plot(time,D,'r',label='Deceased')
plt.legend()
plt.grid()
plt.show()

