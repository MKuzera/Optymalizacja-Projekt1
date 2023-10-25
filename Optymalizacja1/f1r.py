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


def f1r(x, ud1, ud2):
    y0 = np.array([5.0, 1.0, 10.0])
    y = solve_ode(df1, 0, 1, 1000, y0, ud1, x)
    n = y[0].shape[0]
    max = y[1][:, 2].max()
    # nie wiem czy tu przypadkiem nie bedzie po prostu
    # max = y[1][0,2]
    # nizej zaczyna liczyc od 1 wiec raczej to bedzie 0 punkt i dopiero szuka

    
    for i in range(1, n):
        if y[1][i, 2] > max:
            max = y[1][i, 2]

    return np.abs(max - 50)

DA = 0.01
ud1 = np.array(DA)
ud2 = np.array(Dane.Db)

result = f1r(DA, ud1, ud2)

print("Wynik:", result)
