import math
from dane import Dane
import numpy as np
from ekspansji import ekspansja
from fibonacciMethod import fibonacciMethod
from solve_ode import solve_ode
from scipy.integrate import odeint
from matplotlib import pyplot as plt
from lagrange import lagrange
import csv
# 
data=[]
calls=0

ud2 = np.linspace(0, 1000, 1000)
def F1R(ud1,ud2,x):
    global data
    if ud1[0] >= 0:
        res = - Dane.a * Dane.b * x * np.sqrt(2 * Dane.g * ud1[0] / Dane.Pa)
    else:
        res = 0
    d2 = - Dane.a * Dane.b * Dane.Db * np.sqrt(2 * Dane.g * ud1[1] / Dane.Pb) + Dane.Fbin - res
    d3 = (-res * (Dane.Ta - ud1[2]) + Dane.Fbin * (Dane.Tbin - ud1[2])) / ud1[1]
    data.append([ud1[0], ud1[1], ud1[2]])
    return [res, d2, d3]
def write_to_csv(filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Va', 'Vb', 'Tb'])
        for row in data:
            writer.writerow(row)
def fun(x):
    global calls
    calls+=1
    res = odeint(F1R,[Dane.Va,Dane.Vb,Dane.Tb],ud2,args=(x,))
    TBmax = max(res[:,2])
    # print(TBmax)
    return abs(TBmax - 50)

wynik1, wynik2 = ekspansja(fun, 0.0, 0.001, 1.1, 1000)

print(wynik1)
print(wynik2)
data=[]
l=fun(3.3)*(4.2**2.0)
wynikFibo= fibonacciMethod(fun, wynik1, wynik2, 1e-7)
write_to_csv('fibonacci.csv')
data=[]
wynikLagrange = lagrange(wynik1, wynik2, ((wynik1+wynik2)/2), 0.001, 0.0000001, 1000, fun)
write_to_csv('lagrange.csv')


# plt_arg=fun_plt[1][:,2]    
# plt.plot(ud2, plt_arg, label='TB(t)')
# plt.plot(ud2, np.full((len(ud2), 1), 50), label='Max TB')
# plt.xlabel('Czas')
# plt.ylabel('Temperatura')
# plt.legend()
# plt.show()











# def F1R(x,ud1,ud2):
    # y0 = [5.0, 1.0, 10.0]

    # y = SOLVE_ODE(DF1, 0, 1, 1000, y0, ud1, x)
    # n = y[0].shape[0]
    # max = y[1][0, 2]
    # for i in range(1, n):
    #     if y[1][i, 2] > max:
    #         max = y[1][i, 2]
    # return math.abs(max - 50)


    # def DF1(t,Y,ud1,ud2):
#     dY = []
#     DA = ud1
#     DB = Dane.Db
#     Pa = Dane.Pa
#     Pb = Dane.Pb
#     Va = Dane.Va
#     Vb = Dane.Vb
#     Ta = Dane.Ta
#     Tb = Dane.Tb
#     Tbin = Dane.Tbin
#     Fbin = Dane.Fbin
#     a = Dane.a
#     b = Dane.b
#     g = Dane.g
#     if(Y[0] > 0):
#         FAout =  a * b * ud2 * math.sqrt(2*g*Y[0] / Pa)
#     else:
#         FAOut = 0
#     if(Y[1]>1):
#         FBout = a* b * DB * math.sqrt(2*g*Y[1] / Pb)
#     else:
#         Fbout = 0
#     dY[0] = -FAout
#     dY[1] = FAOut + Fbin - Fbout
#     dY[2] = (Fbin / Y[1] * (Tbin - Y[2])) + (FAout / Y[1] * (Ta - Y[2]))

#     return dY