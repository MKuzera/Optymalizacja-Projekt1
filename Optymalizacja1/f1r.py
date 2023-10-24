import solve_ode
import numpy as np
def f1r(x, ud1, ud2, df1):
    y0 = np.array([[5], [1], [10]])
    y = solve_ode(df1, 0, 1, 1000, y0, ud1, x)
    n = y[0].shape[0]
    max = y[1][:, 2].max()
    
    for i in range(1, n):
        if y[1][i, 2] > max:
            max = y[1][i, 2]

    return np.abs(max - 50)