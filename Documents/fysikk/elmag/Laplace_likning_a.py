#--------------- a) ----------------
import numpy as np
import matplotlib.pyplot as plt

N = 100
x = np.linspace(-1, 1, N)
y = np.linspace(-1, 1, N)
dx = x[1] - x[0]
X, Y = np.meshgrid(x, y)
V = np.zeros((N, N))

# Kondensatorposisjon
d = 0.5
x1_idx = np.argmin(np.abs(x + d/2))
x2_idx = np.argmin(np.abs(x - d/2))
y_plate = (Y > -0.5) & (Y < 0.5)

# Randbetingelser
V[:, 0] = 0
V[:, -1] = 0
V[0, :] = 0
V[-1, :] = 0
for j in range(N):
    if -0.5 < y[j] < 0.5:
        V[j, x1_idx] = 1    # venstre plate
        V[j, x2_idx] = -1   # høyre plate

# Iterasjon – Jacobi
V_new = V.copy()
for it in range(5000):
    V_new[1:-1, 1:-1] = 0.25 * (V[2:, 1:-1] + V[:-2, 1:-1] + V[1:-1, 2:] + V[1:-1, :-2])
    # Grensene og platene
    for j in range(N):
        if -0.5 < y[j] < 0.5:
            V_new[j, x1_idx] = 1
            V_new[j, x2_idx] = -1
    V, V_new = V_new, V
    
plt.figure(figsize=(6,5))
plt.imshow(V, extent=[-1, 1, -1, 1], origin='lower', cmap='coolwarm')
plt.colorbar(label='Potensial V')
plt.title("Potensial fra to platekondensatorer (d = 0.5)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

'''Dette heatmapet (a-oppgaven) viser potensialet inne i boksen. Den venstre platen (x = -0.25) er på V = +1, 
    og den høyre platen (x = 0.25) er på V = -1. '
    Potensialet avtar gradvis fra den ene platen til den andre og påvirkes av de jordede veggene.'''
