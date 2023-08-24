from sympy import symbols, Matrix, diff, sin

# Define the variables
R, theta = symbols('R theta')

# Define the metric tensor
g = Matrix([
    [R**2, 0],
    [0, R**2 * sin(theta)**2]
])

# Calculate the derivative of the metric tensor
dg = [[[diff(g[i, j], x) for x in (R, theta)] for j in range(2)] for i in range(2)]

# Calculate the inverse of the metric tensor
g_inv = g.inv()

# Calculate the Christoffel symbols
christoffel = [[[(0.5 * sum(g_inv[i, l] * (dg[j][l][k] + dg[k][l][j] - dg[i][j][k]) 
                 for l in range(2))) for k in range(2)] for j in range(2)] for i in range(2)]

print(christoffel)
