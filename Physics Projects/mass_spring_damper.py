import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from functools import partial

# This is the second problem from the textbook "Python Programming and Numerical Methods"
# Link: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.08-Summary-and-Problems.html

# Defines the differential equation that describes a mass-spring-damper system in one dimension
def my_msd(t, S, m, c, k):
    x, v = S
    dx_dt = v
    dv_dt = -(c * v + k * x) / m
    return [dx_dt, dv_dt]

my_msd(0, [1, -1], 10, 1, 100)

# Constants
m = 1
k = 10

# MSD System with no dampening
f1 = partial(my_msd, m=m, c=0, k=k)
t_e = np.arange(0, 20, 0.1)
sol_1=solve_ivp(f1,[0,20],[1,0],t_eval=t_e)

# MSD System with dampening (c = 1)
f2 = partial(my_msd, m=m, c=1, k=k)
sol_2=solve_ivp(f2,[0,20],[1,0],t_eval=t_e)

# MSD System that is critically dampened
f3 = partial(my_msd, m=m, c=10, k=k)
sol_3=solve_ivp(f3,[0,20],[1,0],t_eval=t_e)

plt.figure(figsize = (10, 8))
plt.plot(sol_1.t, sol_1.y[0])
plt.plot(sol_2.t, sol_2.y[0])
plt.plot(sol_3.t, sol_3.y[0])
plt.title('Numerical Solution of MSD \
System with Varying Dampening')
plt.xlabel('time')
plt.ylabel('displacement')
plt.legend(['No Dampening', 'c = 1', \
           '> Critically Dampened'], loc=1)
plt.show()