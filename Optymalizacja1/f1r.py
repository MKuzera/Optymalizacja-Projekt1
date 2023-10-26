from dane import Dane
import math
import numpy as np
from scipy.integrate import odeint
import pdb

# def df1(t, Y, ud1, ud2):
#     DA = ud1
#     DB = ud2
#     Pa = Dane.Pa
#     Pb = Dane.Pb  # Example value, please replace with actual value
#     Va = Dane.Va  # Example value, please replace with actual value
#     Vb = Dane.Vb  # Example value, please replace with actual value
#     a = Dane.a  # Example value, please replace with actual value
#     b = Dane.b # Example value, please replace with actual value
#     g = Dane.g  # Example value, please replace with actual value
#     Ta = Dane.Ta
#     Tb = Dane.Tb

#     Tadot = (Dane.Fbin * Dane.Tbin - DA * np.sqrt(2 * g * a * (Ta - Tb)) / (Pa * b)) / Va
#     Tbdot = (DA * np.sqrt(2 * g * a * (Ta - Tb)) / (Pa * b) - DB * np.sqrt(2 * g * a * Tb) / (Pb * b)) / Vb

#     return [Tadot, Tbdot]


def df1(t,Y,ud1,ud2):
    dY = []
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
    if(Y[0] > 0):
        FAout =  a * b * ud2 * math.sqrt(2*g*Y[0] / Pa)
    else:
        FAOut = 0
    if(Y[1]>1):
        FBout = a* b * DB * math.sqrt(2*g*Y[1] / Pb)
    else:
        Fbout = 0
    dY[0] = -FAout
    dY[1] = FAOut + Fbin - Fbout
    dY[2] = (Fbin / Y[1] * (Tbin - Y[2])) + (FAout / Y[1] * (Ta - Y[2]))

    return dY

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

