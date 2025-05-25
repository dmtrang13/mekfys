import numpy as np
import matplotlib.pyplot as plt

e_over_m = 1.758820e11  # C/kg

# Magnetfelt B (i gauss, unngår 0)
B_gauss = np.linspace(0.1, 15, 300)
B_tesla = B_gauss * 1e-4  # Konverter til Tesla

# Akselerasjonsspenninger
Ua_values = [20, 40, 60]

plt.figure(figsize=(10, 6))
for Ua in Ua_values:
    r = 1 / B_tesla * np.sqrt(2 * Ua / e_over_m)
    plt.plot(B_gauss, r, label=f'Ua = {Ua} V')

r_max = 0.04  # meter
plt.axhline(y=r_max, color='black', linestyle='--', label='Maks radius (4 cm)')

# Gunstige B-verdier
for Ua in Ua_values:
    B_limit_tesla = (1 / r_max) * np.sqrt(2 * Ua / e_over_m)
    B_limit_gauss = B_limit_tesla * 1e4
    plt.axvline(x=B_limit_gauss, linestyle=':', label=f'B ved Ua={Ua}V ≈ {B_limit_gauss:.1f} G')

plt.title('Radius r som funksjon av magnetfelt B')
plt.xlabel('Magnetfelt B (gauss)')
plt.ylabel('Radius r (meter)')
plt.legend()
plt.grid(True)
plt.ylim(0, 0.1)
plt.show()
