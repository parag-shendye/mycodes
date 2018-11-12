#########################################################
## integrate numerically using euler, heun and collatz ##
#########################################################

import numpy as np
import matplotlib.pyplot as plt

# y'(t)=-cos(t)*y(t), y(0)=1, t=0:50, h=stepsize
h=0.1
t0=0
t1=50
n=t1/h #number of integration points
n=int(n) #convert into integer

#define zero arrays
t=np.zeros([n+1])
yE=np.zeros([n+1]) #Euler
yC=np.zeros([n+1]) #Collatz
yH=np.zeros([n+1]) #Heun

#initial condition
yE[0]=1;
yC[0]=1;
yH[0]=1;

#start numerical integration
for i in range (1,n+1):
  t[i]=0.+i*h
  
  #Forward Euler
  yE[i]= yE[i-1]+h*(-np.cos(t[i-1]))*yE[i-1]
  
  #Collatz
  yC[i]=yC[i-1]+h*(-np.cos(t[i-1]+h/2))*(yC[i-1]+(h/2)*(-np.cos(t[i-1]))*yC[i-1])
  
  #Heun
  c1=-np.cos(t[i-1])*yH[i-1]
  c2=-np.cos(t[i-1]+h)*(yH[i-1]+h*c1)
  yH[i]=yH[i-1]+h/2*(c1+c2)
  

#exact solution
y=np.exp(-np.sin(t)) #functions from math dont play nicely with numpy arrays

#plots
plt.plot(t,y,'r', lw=1.5)
plt.plot(t,yE,'b--')
plt.plot(t,yC,'g')
plt.plot(t,yH,'k')
plt.legend(['Exact','Euler', 'Collatz','Heun'], loc='upper right')
plt.show()





