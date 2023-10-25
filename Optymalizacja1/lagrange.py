# a - poczatek przedzialu
# b - koniec przedzialu
# c - punkt wewnetrzny
# epsilon
# gamma
# Nmax - max ilosc wywołań. (i>Nmax -> error)
# f - funkcja
def lagrange(a, b, c, epsilon, gamma, Nmax, f):

    a=[a]
    b=[b]
    c=[c]
    d = []
    i =0
    for i in range(Nmax):
        l = f(a[i]) * ((b[i]) ** 2 - (c[i]) ** 2) + f(b[i]) * ((c[i]) ** 2 - (a[i]) ** 2) + f(c[i]) * ((a[i]) ** 2 - (b[i]) ** 2)
        m = f(a[i]) * (b[i] - c[i]) + f(b[i]) * (c[i] - a[i]) + f(c[i]) * (a[i] - b[i])
        if(m <= 0):
            return "error3 {}".format(i)
        d.append(0.5*l/m)
        if a[i] < d[i] < c[i]:
            if f(d[i]) < f(c[i]):
                a.append(a[i])
                c.append(d[i])
                b.append(c[i])
            else:
                a.append(d[i])
                c.append(c[i])
                b.append(b[i])
        else:
            if c[i] < d[i] < b[i]:
                if f(d[i]) < f(c[i]):
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
    return d[i]

