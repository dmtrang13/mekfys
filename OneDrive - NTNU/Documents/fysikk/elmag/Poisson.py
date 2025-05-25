import numpy as np
import matplotlib.pyplot as plt

# Define the range for r/R (from 0 to 1.5)
r_R = np.linspace(0, 1.5, 300)

# Define the normalized quantities
rho_norm = np.where(r_R <= 1, (4 - 4 * r_R) / 4, 0)  # ρ(r) / (4ρ0)
Q_norm = np.where(r_R <= 1, (4/3 * r_R**3 - r_R**4) / (4/3), 1)  # Q(r) / (4πρ03R3)
E_norm = np.where(r_R <= 1, (4/3 * r_R - r_R**2) / (4/3), 1/r_R**2)  # E(r) / (ρ03ε0R)
V_norm = np.where(r_R <= 1, (1 - (2/3) * (r_R**2 - 1) + (1/3) * (r_R**3 - 1)), 1/r_R)  # V(r) / (ρ03ε0R2)

# Plot all the functions
plt.figure(figsize=(8, 6))

plt.plot(r_R, rho_norm, label=r"$\rho(r/R) / 4\rho_0$", linestyle='-', color='b')
plt.plot(r_R, Q_norm, label=r"$Q(r/R) / 4\pi\rho_0 3R^3$", linestyle='--', color='g')
plt.plot(r_R, E_norm, label=r"$E(r/R) / \rho_0 3\epsilon_0 R$", linestyle='-.', color='r')
plt.plot(r_R, V_norm, label=r"$V(r/R) / \rho_0 3\epsilon_0 R^2$", linestyle=':', color='m')

# Labels and Legend
plt.xlabel(r"$r/R$", fontsize=12)
plt.ylabel("Normalized Values", fontsize=12)
plt.title("Dimensionless Plots of Charge Density, Charge, Electric Field, and Potential", fontsize=14)
plt.legend()
plt.grid(True)

# Show plot
plt.show()
