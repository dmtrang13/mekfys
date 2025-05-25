#--------------- c) ----------------
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
    

d_vals = np.linspace(0.2, 0.8, 30)
E_strengths = []

for d in d_vals:
    V = np.zeros((N, N))
    x1_idx = np.argmin(np.abs(x + d/2))
    x2_idx = np.argmin(np.abs(x - d/2))
    for j in range(N):
        if -0.5 < y[j] < 0.5:
            V_new[j, x1_idx] = 1
            V_new[j, x2_idx] = -1
    V_new = V.copy()
    for _ in range(1000):
        V_new[1:-1, 1:-1] = 0.25 * (V[2:, 1:-1] + V[:-2, 1:-1] + V[1:-1, 2:] + V[1:-1, :-2])
        for j in range(N):
            if -0.5 < y[j] < 0.5:
                V_new[j, x1_idx] = 1
                V_new[j, x2_idx] = -1
        V, V_new = V_new, V

    Ey, Ex = np.gradient(-V, dx, dx)
    i = np.argmin(np.abs(x - 0.0))
    j = np.argmin(np.abs(y - 0.6))
    E_strength = np.sqrt(Ex[j, i]**2 + Ey[j, i]**2)
    E_strengths.append(E_strength)

plt.plot(d_vals, E_strengths)
plt.xlabel("Plateseparasjon d")
plt.ylabel("Feltstyrke i punkt (0, 0.6)")
plt.title("Feltstyrke vs plateseparasjon")
plt.grid(True)
plt.show()

'''Plottet viser hvordan feltstyrken i punktet rett over midten mellom platene minker når platene flyttes fra hverandre.
    Dette stemmer med forventningen: større avstand gir svakere felt i området mellom.'''
