def ekspansja(f,x0,d,alpha,nmax):

    i = 0
    x = []
    x.append(x0)
    x.append(x0+d)
    if(f(x[1]) == f(x[0])):
        return [x[0],x[1]]
    if(x[1] > f(x0)):
        d= -d
        x[1] = x[0] + d
        if(f(x[1]) >= f(x[0])):
            return [x[1],x[0]-d]

    while f(x[i]) >= f(x[i+1]):
       # print("15")
        if(i > nmax):
            return "error"
        i= i+1
        x.append(x[0] + pow(alpha,i)*d)
    if d>0:
        return [x[i-1],x[i+1]]
    return [x[i+1],x[i-1]]
