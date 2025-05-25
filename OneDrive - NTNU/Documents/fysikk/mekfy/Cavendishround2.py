import matplotlib.pyplot as plt # alle plottefunksjoner
import numpy as np # inneholder en type array som er enkle og raske å jobbe med
from scipy.optimize import curve_fit # Funksjon for kurvetilpasning

filnavn = "C:\\Users\\duong\\Cavendishround2.txt" # [minutter, sekunder, S (mm)]

###################################################################
## Hvis tilpasningen feiler kan dere endre de initielle verdiene ##
###################################################################
S0_0 = 460    # Likevektslinje
A0 = 20       # Amplitude, svingeutslag
alpha0 = 0    # Eksponensiell dempingskoeffisient for amplituden
T0 = 650      # Periode
phi0 = 0.6    # Fasevinkel
###################################################################

###############################################
## Her kan vi legge til en usikkerhet i S(t) ##
###############################################
dSt = 10 #mm
###############################################

def svingeutslag(t, S, A, alpha, w, phi):
    #   Modell for harmonisk svingning
    #   S(t) = S_0 + A*exp(-alpha*t)*sin(omega*t + phi)
    return S + A*np.exp(-alpha*t)*np.sin(w*t + phi)

def tilpass(S, t, p0):
    # Vi prøver å tilpasse modelfunksjonen til datasettet
    # Denne funksjonen minimerer kvadratfeilen sum((x - x_data)^2)
    params, cov = curve_fit(svingeutslag, t, S, p0=p0, sigma=len(S)*[dSt], absolute_sigma=True)
    # Variansen ligger i diagonalen til kovariansmatrisa
    # Standardavviket er kvadratroten av dette
    return params, np.sqrt(np.diag(cov))

# Leser datafilen
D = np.loadtxt(filnavn)
t = D[:, 0]*60 + D[:, 1]    # tid i s
S = D[:, 2]                 # Svingeutslag i mm

# Kaller tilpasningsfunksjonen vår
p, perr = tilpass(S, t, [S0_0, A0, alpha0, 2*np.pi/T0, phi0])
[S0, A, alpha, w, phi] = p
[dS0, dA, dalpha, dw, dphi] = perr

# Perioden er
#T = 2*np.pi/w
# men dempingen i Cavendish-eksperimentet kan bli tatt høyde for ved å
# heller bruke perioden til den tilsvarende ikke-dempede svingningen
T = 2*np.pi/(w**2 + alpha**2)**.5

# Vi printer til slutt resultatet
print('Tilpassede verdier:\nS0=\t\t%e mm\nA=\t\t%e mm\nAlpha=\t%e 1/s\nw=\t\t%e (rad)/s\nT0=\t\t%e s\nphi=\t%e (rad)' % 
    (S0, A, alpha, w, T, phi))
print('Usikkerheter:\ndS0=\t%e mm\ndA=\t\t%e mm\ndAlpha=\t%e1/s\ndw=\t\t%e (rad)/s\ndphi=\t%e (rad)' %
    (dS0, dA, dalpha, dw, dphi))

###################################
## Her kan dere endre på figuren ##
###################################
t_plot = np.linspace(t[0], t[-1], 100)
plt.figure('Figur 1')
plt.plot(t, S, 'bx', label='Målte data')
plt.plot(t_plot, svingeutslag(t_plot, *p), '-r', label='$S(t)=%f%+f*e^{-%f*t}*\sin(%f*t%+f)$' %
    (S0, A, alpha, w, phi))
plt.plot(t_plot, S0*np.ones(len(t_plot)), 'k')        # Likevektslinje
plt.plot(t_plot, S0 + A*np.exp(-alpha*t_plot), '--k')   # Øvre omhyldningskurve
plt.plot(t_plot, S0 - A*np.exp(-alpha*t_plot), '--k')   # Nedre omhyldningskurve
plt.xlabel('Tid (s)')
plt.ylabel('Svingeutslag (mm)')
plt.legend()
plt.show()
###################################
