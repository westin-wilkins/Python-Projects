import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np

# Lotka-Volterra equations
def lotka_volterra(t, y, alpha, beta, gamma, delta):
    x, y = y
    dx_dt = alpha * x - beta * x * y
    dy_dt = delta * x * y - gamma * y
    return [dx_dt, dy_dt]

# Constants
t_span = [0, 20]
alpha = 1
beta = 1.5

soln = integrate.solve_ivp(lotka_volterra, t_span, [1, 1], args=(alpha, beta, 1, 1), t_eval=np.linspace(t_span[0], t_span[1], 10000))

# Extract solutions
X, Y, = soln.y

# Plot solutions
fig = plt.figure(figsize = (10,10))
ax = plt.axes()
ax.grid()

ax.plot(soln.t, X, label='Prey')
ax.plot(soln.t, Y, label='Predator')
ax.legend()
plt.show()