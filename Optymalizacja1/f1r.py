from dane import Dane
import math
import numpy as np
from scipy.integrate import odeint
import pdb

def df1(t, Y, ud1, ud2):
    DA = ud1
    DB = ud2
    Pa = Dane.Pa
    Pb = Dane.Pb  # Example value, please replace with actual value
    Va = Dane.Va  # Example value, please replace with actual value
    Vb = Dane.Vb  # Example value, please replace with actual value
    a = Dane.a  # Example value, please replace with actual value
    b = Dane.b # Example value, please replace with actual value
    g = Dane.g  # Example value, please replace with actual value
    Ta = Dane.Ta
    Tb = Dane.Tb

    Tadot = (Dane.Fbin * Dane.Tbin - DA * np.sqrt(2 * g * a * (Ta - Tb)) / (Pa * b)) / Va
    Tbdot = (DA * np.sqrt(2 * g * a * (Ta - Tb)) / (Pa * b) - DB * np.sqrt(2 * g * a * Tb) / (Pb * b)) / Vb

    return [Tadot, Tbdot]

def f1r(x, ud1, ud2):
    y0 = [5.0, 10.0]  # Initial values of Ta and Tb
    t = np.linspace(0, 1000, 1001)  # Time points from 0 to 1000

    y = odeint(df1, y0, t, args=(ud1, ud2))

    max_Tb = y[:, 1].max()

    return np.abs(max_Tb - 50)

DA = 0.01
ud1 = DA
ud2 = Dane.Db   # Assuming Dane.Db is a valid constant

result = f1r(0, ud1, ud2)

print("Wynik:", result)

