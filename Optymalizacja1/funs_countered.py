import math

calls = 0

def funckja_celu(x):
    global calls
    calls = calls + 1
    return -1 * math.cos(0.1 * x) * pow(math.e, -1 * pow(0.1 * x - 2 * math.pi, 2)) + 0.002 * pow(0.1 * x, 2)




def fibonacciMethod(a, b, e):
    global calls
    calls = 0
    if (e < 0 or (b < a)):
        return "ERROR, bad input at fibonacciMethod"
    fib = [0, 1]
    k = 1
    while fib[k] < (b - a) / e:
        fib.append(fib[-2] + fib[-1])
        k += 1
    A = [a]
    B = [b]
    C = [B[0] - fib[k - 1] / fib[k] * (B[0] - A[0])]
    D = [A[0] + B[0] - C[0]]
    for i in range(k - 3):

        if funckja_celu(C[i]) < funckja_celu(D[i]):
            A.append(A[i])
            B.append(D[i])
        else:
            B.append(B[i])
            A.append(C[i])

        C.append(B[i + 1] - fib[k - i - 2] / fib[k - i - 1] * (B[i + 1] - A[i + 1]))
        D.append(A[i + 1] + B[i + 1] - C[i + 1])

    return [C[i + 1],calls]

def lagrange(a, b, c, epsilon, gamma, Nmax):

    global calls
    calls = 0
    a=[a]
    b=[b]
    c=[c]
    d = []
    i =0
    for i in range(Nmax):
        l = funckja_celu(a[i]) * ((b[i]) ** 2 - (c[i]) ** 2) + funckja_celu(b[i]) * ((c[i]) ** 2 - (a[i]) ** 2) + funckja_celu(c[i]) * ((a[i]) ** 2 - (b[i]) ** 2)
        m = funckja_celu(a[i]) * (b[i] - c[i]) + funckja_celu(b[i]) * (c[i] - a[i]) + funckja_celu(c[i]) * (a[i] - b[i])
        if(m <= 0):
            return "error3 {}".format(i)
        d.append(0.5*l/m)
        if a[i] < d[i] < c[i]:
            if funckja_celu(d[i]) < funckja_celu(c[i]):
                a.append(a[i])
                c.append(d[i])
                b.append(c[i])
            else:
                a.append(d[i])
                c.append(c[i])
                b.append(b[i])
        else:
            if c[i] < d[i] < b[i]:
                if funckja_celu(d[i]) < funckja_celu(c[i]):
                    a.append(c[i])
                    c.append(d[i])
                    b.append(b[i])
                else:
                    a.append(a[i])
                    c.append(c[i])
                    b.append(d[i])
            else:
                return "error4"

        if(b[i] - a[i] < epsilon or abs(d[i] - d[i-1]) < gamma):
            break
    return [d[i],calls]

def ekspansja(x0,d,alpha,nmax):
    global calls
    calls = 0
    i = 0
    x = []
    x.append(x0)
    x.append(x0+d)
    if(funckja_celu(x[1]) == funckja_celu(x[0])):
        return [x0,x[0],x[1],calls]
    if(x[1] > funckja_celu(x0)):
        d= -d
        x[1] = x[0] + d
        if(funckja_celu(x[1]) >= funckja_celu(x[0])):
            return [x0,x[1],x[0]-d,calls]

    while funckja_celu(x[i]) >= funckja_celu(x[i+1]):
        if(i > nmax):
            return "error"
        i= i+1
        x.append(x[0] + pow(alpha,i)*d)
    if d>0:
        return [x0,x[i-1],x[i+1],calls]
    return [x0,x[i+1],x[i-1],calls]

