from solve_ode import solve_ode
import numpy as np
from dane import Dane
from scipy.integrate import solve_ivp

def df1(t, Y, ud1, ud2):
    DA = ud1
    DB = Dane.Db
    Pa = Dane.Pa
    Pb = Dane.Pb
    Va = Dane.Va
    Vb = Dane.Vb
    Ta = Dane.Ta
    Tb = Dane.Tb
    Tbin = Dane.Tbin
    Fbin = Dane.Fbin
    a = Dane.a
    b = Dane.b
    g = Dane.g

    Tadot = (Fbin * Tbin - DA * np.sqrt(2 * g * a * (Ta - Y[0])) / (Pa * b)) / Va
    Tbdot = (DA * np.sqrt(2 * g * a * (Ta - Y[0])) / (Pa * b) - DB * np.sqrt(2 * g * a * (Y[1] - Tb)) / (Pb * b)) / Vb
    return np.array([Tadot, Tbdot]).reshape((2, 1))

def f1r(x, ud1, ud2):
    y0 = np.array([5.0, 1.0, 10.0])
    y = solve_ode(df1, 0, 1, 1000, y0, ud1, x)
    n = y[0].shape[0]
    max = y[1][:, 2].max()
    
    for i in range(1, n):
        if y[1][i, 2] > max:
            max = y[1][i, 2]

    return np.abs(max - 50)
DA = 0.01
ud1 = np.array(DA)
ud2 = np.array(Dane.Db)

result = f1r(DA, ud1, ud2)

print("Wynik:", result)
