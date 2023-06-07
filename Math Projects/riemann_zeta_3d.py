import numpy as np
import matplotlib.pyplot as plt


# Computes the Riemann zeta function up to the N'th term with parameter s
def zeta(s, N = 100):
    zeta_series = 0
    
    for N in range(1, N + 1):
        zeta_series += 1 / N**s 
    return zeta_series

real_vals = np.linspace(-10.0, 10.0, 100)
imag_vals = np.linspace(-10.0, 10.0, 100)
real, imag = np.meshgrid(real_vals, imag_vals)
s = real + 1j*imag

# Compute the zeta function for each value of s
z = zeta(s)

# Create a 3D surface plot of the real and imaginary parts of the zeta function
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(real, imag, np.real(z), cmap='viridis')
ax.plot_surface(real, imag, np.imag(z), cmap='viridis')
ax.set_xlabel('Real(s)')
ax.set_ylabel('Imag(s)')
ax.set_zlabel('Real(zeta(s)), Imag(zeta(s))')
plt.title('Riemann Zeta Function')
plt.show()