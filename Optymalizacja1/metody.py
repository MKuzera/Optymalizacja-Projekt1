import math
from dane import *
import numpy as np
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


#df1 powinno zwracac macierz [x,x,x]

#matrix df1(double t, matrix Y, matrix ud1, matrix ud2)
#{
#matrix dY(3, 1);
#double a = 0.98, b = 0.63, g = 9.81, PA = 0.75, TA = 90, PB = 1.0, DB = 0.00365665, Fin = 0.01, Tin= 10;
#double FAout = Y(0)>0? a * b * m2d(ud2) * sqrt(2 * g * Y(0) / PA):0;
#double FBout = Y(1)>1?a * b * DB * sqrt(2 * g * Y(1) / PB):0;
#dY(0) = -FAout;
#dY(1) = FAout + Fin - FBout;
#dY(2) = Fin / Y(1) * (Tin - Y(2)) + FAout / Y(1) * (TA - Y(2));
#// std::cout << dY << std::endl;
#return dY;
#}


def F1R(x,ud1,ud2):
    y0 = [5.0, 1.0, 10.0]
    y = SOLVE_ODE(DF1, 0, 1, 1000, y0, ud1, x)
    n = y[0].shape[0]
    max = y[1][0, 2]
    for i in range(1, n):
        if y[1][i, 2] > max:
            max = y[1][i, 2]
    return math.abs(max - 50)


def SOLVE_ODE():

    pass

# ??? edytowac
def Solve_ode(diff, t0, dt, tend, Y0, ud1, ud2):
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