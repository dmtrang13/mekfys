import numpy as np
import matplotlib.pyplot as plt

# Define constants
rho_0 = 1  # Arbitrary constant for scaling (since we only care about shape)
epsilon_0 = 1  # Normalized permittivity
t = 1  # Thickness of the plate

# Define z values
z_inside = np.linspace(-t, t, 100)  # Inside the plate
z_outside_left = np.linspace(-2*t, -t, 50)  # Left outside region
z_outside_right = np.linspace(t, 2*t, 50)  # Right outside region

# Compute |E(z)| inside the plate
E_inside = (rho_0 / epsilon_0) * (2 * t / np.pi) * np.sin((np.pi / 2) * (z_inside / t))

# Compute |E(z)| outside the plate (constant)
E_outside_left = [(rho_0 / epsilon_0) * (2 * t / np.pi)] * len(z_outside_left)
E_outside_right = [(rho_0 / epsilon_0) * (2 * t / np.pi)] * len(z_outside_right)

# Combine values for plotting
z_values = np.concatenate([z_outside_left, z_inside, z_outside_right])
E_values = np.concatenate([np.abs(E_outside_left), np.abs(E_inside), np.abs(E_outside_right)])

# Plot the corrected graph
plt.figure(figsize=(8, 5))
plt.plot(z_values, E_values, label=r'$|E(z)|$', color='b')

# Mark transition points correctly
plt.axvline(x=-t, linestyle='--', color='r', alpha=0.6, label=r'$z = \pm t$')
plt.axvline(x=t, linestyle='--', color='r', alpha=0.6)


# Labels and title
plt.xlabel(r'$z$ (position)')
plt.ylabel(r'$|E(z)|$ (Electric Field Magnitude)')
plt.title(r'Plot of $|E(z)|$ vs. $z$')
plt.legend()
plt.grid()

# Show the plot
plt.show()
