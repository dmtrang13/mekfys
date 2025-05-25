import numpy as np
import matplotlib.pyplot as plt

# Define constants for visualization
rho_0 = 1   # Assume unit charge density for scaling
epsilon = 1  # Assume unit permittivity
t = 1        # Assume unit half-thickness
pi = np.pi

# Define z values for inside and outside regions
z_inside = np.linspace(-t, t, 100)
z_outside_left = np.linspace(-2*t, -t, 50)
z_outside_right = np.linspace(t, 2*t, 50)

# Compute V(z) inside the plate
V_inside = (rho_0 / epsilon) * (4 * t**2 / pi**2) * (np.cos((pi / 2) * (z_inside / t)) - 1)

# Compute V(z) outside the plate (linear functions)
V_t = (rho_0 / epsilon) * (-4 * t**2 / pi**2)  # Value at z = ±t
V_outside_left = (rho_0 / epsilon) * (2 * t / pi) * (z_outside_left + t) + V_t
V_outside_right = (rho_0 / epsilon) * (2 * t / pi) * (t - z_outside_right) + V_t

# Combine z values for plotting
z_values = np.concatenate([z_outside_left, z_inside, z_outside_right])
V_values = np.concatenate([V_outside_left, V_inside, V_outside_right])

# Plot the potential
plt.figure(figsize=(8, 5))
plt.plot(z_values, V_values, label=r'$V(z)$', color='b')
plt.axvline(x=-t, linestyle='--', color='r', alpha=0.6, label=r'$z = \pm t$')
plt.axvline(x=t, linestyle='--', color='r', alpha=0.6)

# Labels and title
plt.xlabel(r'$z$ (position)')
plt.ylabel(r'$V(z)$ (Electric Potential)')
plt.title(r'Plot of $V(z)$ vs. $z$')
plt.legend()
plt.grid()

# Show the plot
plt.show()
