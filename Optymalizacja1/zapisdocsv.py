import csv
import math
from random import randint

from funs_countered import ekspansja
from funs_countered import fibonacciMethod
from funs_countered import lagrange
przybliz = 0.00001
def fibonacci_do_csv(all):
    data = [['x', 'y', 'calls', 'min']]
    for i in range(0, 300):
        fib_data = fibonacciMethod(all[i][1],all[i][2],0.00001)
        row = [fib_data[0],  fib_data[1],  fib_data[2],  fib_data[3]]
        data.append(row)
    with open('daneCSV/daneFIBNOCACCI.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

def lagrange_do_csv(all):
    data = [['x', 'y', 'calls', 'min']]
    for i in range(0, 300):
        lagrange_data = lagrange(all[i][1],all[i][2],(all[i][1]+all[i][2]) /2,0.00001,0.00001,1000)
        row = [lagrange_data[0],  lagrange_data[1],  lagrange_data[2],  lagrange_data[3]]
        data.append(row)
    with open('daneCSV/daneLAGRANGE.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)




def ekspansja_do_csv():
    all = []
    data = []
    for i in range(1, 101):
       ekspansja_data = ekspansja(randint(-100, 100), 1.0, 2.0, 1000)
       row = [ekspansja_data[0], ekspansja_data[1], ekspansja_data[2], ekspansja_data[3]]
       data.append(row)

    with open('daneCSV/daneEKSPANSJIalfa20.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
    all += data
    data = []
    for i in range(1, 101):
        ekspansja_data = ekspansja(randint(-100, 100), 1.0, 1.5, 1000)
        row = [ekspansja_data[0], ekspansja_data[1], ekspansja_data[2], ekspansja_data[3]]
        data.append(row)
    with open('daneCSV/daneEKSPANSJIalfa15.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
    all += data
    data = []
    for i in range(1, 101):
        ekspansja_data = ekspansja(randint(-100, 100), 1.0, 1.2, 1000)
        # Przypisz wartości do odpowiednich kolumn
        row = [ekspansja_data[0], ekspansja_data[1], ekspansja_data[2], ekspansja_data[3]]
        data.append(row)
    with open('daneCSV/daneEKSPANSJIalfa12.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
    all += data
    return all
