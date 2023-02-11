import numpy as np
# This program calculates the half life a given element.
# Decay constant of U235 - 9.72e-10 (yr-1)
# Decay constnat of U238 - 1.54e-10 (yr-1)
# Decay constant of C14 - 3.8394e-12 (yr-1)
# Decay constant of PU239 - 2.88e-5 (yr-1)

decay_constant = 1.54e-10

half_life = -np.log(2)/decay_constant # Time it takes for element to reach its half life

print(f"The half-life of the given element is approximately {half_life} (yr-1).")
