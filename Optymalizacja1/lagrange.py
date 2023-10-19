def lagrange(a, b, c, epsilon, gamma, Nmax, f):
    i = 0
    a_i, b_i, c_i = a, b, c
    d_i = 0
    
    while True:
        l = f(a_i) * ((b_i**2 - c_i**2)) + f(b_i) * ((c_i**2 - a_i**2)) + f(c_i) * ((a_i**2 - b_i**2))
        m = f(a_i) * (b_i - c_i) + f(b_i) * (c_i - a_i) + f(c_i) * (a_i - b_i)
        
        if m <= 0:
            return "Error"
        
        d_i = 0.5 * l / m
        
        if a_i < d_i < c_i:
            if f(d_i) < f(c_i):
                a_i_1 = a_i
                c_i_1 = d_i
                b_i_1 = c_i
            else:
                a_i_1 = d_i
                c_i_1 = c_i
                b_i_1 = b_i
        elif c_i < d_i < b_i:
            if f(d_i) < f(c_i):
                a_i_1 = c_i
                c_i_1 = d_i
                b_i_1 = b_i
            else:
                a_i_1 = a_i
                c_i_1 = c_i
                b_i_1 = d_i
        else:
            return "Error"
        
        i += 1
        
        if i > Nmax:
            return "Error"
        
        if (b_i_1 - a_i_1 < epsilon) or (abs(d_i - d_i_1) < gamma):
            return d_i_1

        a_i = a_i_1
        b_i = b_i_1
        c_i = c_i_1
