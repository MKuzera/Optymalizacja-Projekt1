# import math

# from solve_ode import solve_ode
# import numpy as np
from dane import Dane
# from scipy.integrate import solve_ivp, odeint

# def df1(t, Y, ud1, ud2):
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

#     Tadot = (Fbin * Tbin - DA * np.sqrt(2 * g * a * (Ta - Y[0])) / (Pa * b)) / Va
#     Tbdot = (DA * np.sqrt(2 * g * a * (Ta - Y[0])) / (Pa * b) - DB * np.sqrt(2 * g * a * (Y[1] - Tb)) / (Pb * b)) / Vb
#     return np.array([Tadot, Tbdot]).reshape((2, 1))



# def f1r(x, ud1, ud2):
#     y0 = np.array([5.0, 1.0])  # Changed to 1D array
#     y = odeint(df1, y0, np.array([0, 1000]), args=(ud1, ud2))  # Fixed the function call
#     n = y.shape[0]  # Corrected to use y.shape[0]
#     max = y[:, 1].max()  # Changed indexing to reflect new shape

#     for i in range(1, n):
#         if y[i, 1] > max:
#             max = y[i, 1]

#     return np.abs(max - 50)


# DA = 0.01
# ud1 = np.array(DA)
# ud2 = np.array(Dane.Db)

# result = f1r(DA, ud1, ud2)

# print("Wynik:", result)

import math
import numpy as np
from scipy.integrate import odeint
import pdb

def df1(t, Y, ud1, ud2):
    DA = ud1
    DB = ud2
    Pa = 100000  # Example value, please replace with actual value
    Pb = 100000  # Example value, please replace with actual value
    Va = 1.0  # Example value, please replace with actual value
    Vb = 1.0  # Example value, please replace with actual value
    a = 1.0  # Example value, please replace with actual value
    b = 1.0  # Example value, please replace with actual value
    g = 9.81  # Example value, please replace with actual value
    # pdb.set_trace()
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
ud2 = 0.02  # Assuming Dane.Db is a valid constant

result = f1r(0, ud1, ud2)

print("Wynik:", result)

