import math

from fibonacciMethod import *
from zapisdocsv import *
from ekspansji import  *;
from lagrange import *;


# sprawdzenie czy funkcje dzialaja prawidlowo:
def funckja_celu(x):
    return -1 * math.cos(0.1*x) * pow(math.e ,-1*pow(0.1*x - 2*math.pi,2)) + 0.002*pow(0.1*x,2)

#ekspansji dziala!
print(ekspansja(funckja_celu,100,1.0,2.0,1000))
#fibonacciego dziala!

x = fibonacciMethod(funckja_celu,-10,10,0.00001)
print(x)

#ekspansja_do_csv()

#print(funckja_celu(x))
#lagrange dziala!

print("WYNIK")
print(lagrange(-100,100,0,0.0001,0.00001,1000,funckja_celu))






