# f - funkcja
# x0 - punkt startowy
# d - odleglosc (x1 -x0)
# alpha - wsp ekspansji
# nmax - maks ilosc iteracji
# i - Liczba wywolan funkcji celu

def ekspansja(f,x0,d,alpha,nmax):

    i = 0
    x = []
    x.append(x0)
    x.append(x0+d)
    if(f(x[1]) == f(x[0])):
        return [x[0],x[1],x[0],i]
    if(x[1] > f(x0)):
        d= -d
        x[1] = x[0] + d
        if(f(x[1]) >= f(x[0])):
            return [x[1],x[0]-d,x[0],i]

    while f(x[i]) >= f(x[i+1]):
       # print("15")
        if(i > nmax):
            return "error"
        i= i+1
        x.append(x[0] + pow(alpha,i)*d)
    if d>0:
        return [x[i-1],x[i+1],x[0],i]
    #zwraca [a,b,x0,i] - 4 dane potrzebne do tabelki
    # i - ilosc wywolan
    return [x[i+1],x[i-1],x[0],i]
