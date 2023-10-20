from dane import *

def golden_section_search(f, x0, d, alpha, Nmax):
    x = [x0, x0 + d]
    fcalls = 2
    
    if f(x[1]) == f(x[0]):
        return x

    if f(x[1]) > f(x[0]):
        d = -d
        x[1] = x[0] + d
        
        if f(x[1]) >= f(x[0]):
            return [x[1], x[0] - d]
    
    i = 0
    while fcalls <= Nmax:
        i += 1
        x.append(x[0] + (alpha**i) * d)
        fcalls += 1
        
        if f(x[i]) > f(x[i+1]):
            break
    
    if d > 0:
        return [x[i-1], x[i+1]]
    else:
        return [x[i+1], x[i-1]]
