# f - funkcja przekazywana
# a - początek przedziału poszukiwań
# b - koniec przedziału poszukiwań
# e - dokładnosc obliczeń (e > 0)
def fibonacciMethod(f,a,b,e):
    if(e < 0 or (b<a)):
        return "ERROR, bad input"
    fib = [0,1]
    k=1
    while fib[k] < (b - a) / e:
        fib.append(fib[-2] + fib[-1])
        k += 1

    A = [a]
    B = [b]
    C = [B[0] - fib[k - 1] / fib[k] * (B[0] - A[0])]
    D = [A[0] + B[0] - C[0]]

    for i in range(k - 3):
        if f(C[i]) < f(D[i]):
            A.append(A[i])
            B.append(D[i])
        else:
            B.append(B[i])
            A.append(C[i])

        C.append(B[i + 1] - fib[k - i - 2] / fib[k - i - 1] * (B[i + 1] - A[i + 1]))
        D.append(A[i + 1] + B[i + 1] - C[i + 1])

    return C[i + 1]

