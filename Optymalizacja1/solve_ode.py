import numpy as np

def solve_ode(diff, t0, dt, tend, Y0, ud1, ud2):
    try:
        N = int(np.floor((tend - t0) / dt) + 1)
        if N < 2:
            raise Exception("solve_ode: Time interval is not defined correctly")
        
        n, _ = Y0.shape
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