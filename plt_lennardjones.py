import numpy as np
import matplotlib.pyplot as plt


#define parameter for LJ
eps=1.
sig=1.
r_cut=2.5*sig

r_ij=np.arange(0.1,r_cut,0.001)  # define vector [float1,...,float2]


u_LJ=4*eps*((sig/r_ij)**12-(sig/r_ij)**6)
u_LJ2=4*2*eps*((sig/r_ij)**12-(sig/r_ij)**6)
f_LJ=48*eps/r_ij*((sig/r_ij)**12-0.5*(sig/r_ij)**6) # eq.(10) in exercise 3

# for zero line
l=len(r_ij)
z=np.zeros(l)

plt.xlim([0.75*sig,r_cut])
plt.ylim([-3,3])

plt.plot(r_ij,z,'g',lw=1)
plt.plot(r_ij,u_LJ,'r',lw=2)
plt.plot(r_ij,u_LJ2,'b',lw=2)

plt.legend(['zero line', 'potential', 'potential2'], loc='upper right')

plt.show()

