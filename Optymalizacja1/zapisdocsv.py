import csv
import math
from ekspansji import ekspansja
from fibonacciMethod import fibonacciMethod




def funckja_celu(x):
    return -1 * math.cos(0.1*x) * pow(math.e ,-1*pow(0.1*x - 2*math.pi,2)) + 0.002*pow(0.1*x,2)

# nie dotykac ;)



# DLA EKSPANSJI :
#
#data = [['a', 'b', 'x', 'n']]  # Nagłówki kolumn
#for i in range(1, 101):
#    data.append(ekspansja(funckja_celu,84,1.0,1.2,1000))
#
#with open('daneLagrangealfa12.csv', 'w', newline='') as csvfile:
#    csv_writer = csv.writer(csvfile)
#    csv_writer.writerows(data)



