# Mass of the earth 5.97219e24 (kg)
# Mass of the sun 1.9891e30 (kg)
# Mass of Jupiter 1.89813e27 (kg)
# Mass of Mercury 3.285e23 (kg)

g = 6.674E-11 # Gravitational constant 
c = 299792458 # Speed of light
m = (float(input("Input a mass in (kg): "))) # Mass

Schwarzchild_radius = 2*g*m/c**2

print(f'The Schwarzchild radius is {Schwarzchild_radius * 100} (cm)') # The 100 converts m to cm
