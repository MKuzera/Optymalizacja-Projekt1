import math
from dane import *
import numpy as np
from ekspansji import ekspansja
from solve_ode import solve_ode
from scipy.integrate import odeint
def DF1(t,Y,ud1,ud2):
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
    dY[1] = FAOut + Fbin - Fbout;
    dY[2] = (Fbin / Y[1] * (Tbin - Y[2])) + (FAout / Y[1] * (Ta - Y[2]))

    return dY



def F1R(x,ud1,ud2):
    y0 = [5.0, 1.0, 10.0]

    y = SOLVE_ODE(DF1, 0, 1, 1000, y0, ud1, x)
    n = y[0].shape[0]
    max = y[1][0, 2]
    for i in range(1, n):
        if y[1][i, 2] > max:
            max = y[1][i, 2]
    return math.abs(max - 50)

t = np.linspace(0, 1000, 1001)
def fun(Da):
    res = odeint(DF1,[Dane.Va,Dane.Vb,Dane.Tb],t,args=(Da,Da))
    TBmax = max(res[:,2])
    return abs(TBmax - 50)

wynik = ekspansja(fun,0.0,0.001,1.2,1000)
print(wynik)


def SOLVE_ODE(diff, t0, dt, tend, Y0, ud1, ud2):
    try:
        N = int(np.floor((tend - t0) / dt) + 1)
        if N < 2:
            raise Exception("solve_ode: Time interval is not defined correctly")

        _, n = Y0.shape
        if n != 1:
            raise Exception("solve_ode: Initial condition must be a column vector")

        S = [np.zeros((N, 1)), np.zeros((n, N))]

        S[0][0] = t0
        S[1][:, 0] = Y0[:, 0]

        k1, k2, k3, k4 = np.zeros((n, 1)), np.zeros((n, 1)), np.zeros((n, 1)), np.zeros((n, 1))

        for i in range(1, N):
            S[0][i] = S[0][i - 1] + dt
            t_prev, Y_prev = S[0][i - 1], S[1][:, i - 1]

            k1 = dt * diff(t_prev, Y_prev, ud1, ud2)
            k2 = dt * diff(t_prev + 0.5 * dt, Y_prev + 0.5 * k1, ud1, ud2)
            k3 = dt * diff(t_prev + 0.5 * dt, Y_prev + 0.5 * k2, ud1, ud2)
            k4 = dt * diff(t_prev + dt, Y_prev + k3, ud1, ud2)

            S[1][:, i] = Y_prev + (k1 + 2 * k2 + 2 * k3 + k4) / 6

        S[1] = S[1].T
        return S

    except Exception as ex_info:
        raise Exception(f"solve_ode: {str(ex_info)}")
    

