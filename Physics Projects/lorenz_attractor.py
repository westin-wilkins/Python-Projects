import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# This is the first problem from the textbook "Python Programming and Numerical Methods"
# Link: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter22.08-Summary-and-Problems.html

# Defines the Lorenz Attractor
def my_lorenz_solver(t, s0, sigma, rho, beta):
    x, y, z = s0
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    
    return [dx_dt, dy_dt, dz_dt]

# Constants
sigma = 10
rho = 28
beta = 8/3
t_span = [0, 50] # Time span for integration from t0 to tf
s0 = np.array([0, 1, 1.05]) # Initail conditions

soln = solve_ivp(my_lorenz_solver, t_span, s0, args=(sigma, rho, beta), 
                 t_eval=np.linspace(t_span[0], t_span[1], 10000))

# Extracts solutions
X, Y, Z = soln.y

fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')
ax.grid()

ax.plot3D(X, Y, Z)

# Set axes label
ax.set_xlabel('x', labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('z', labelpad=20)

plt.show()
