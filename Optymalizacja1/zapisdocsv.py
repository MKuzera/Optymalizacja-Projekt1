import csv
import math
from random import randint

from funs_countered import ekspansja
from fibonacciMethod import fibonacciMethod




def ekspansja_do_csv():
    data = [['x', 'a', 'b', 'calls']]
    for i in range(1, 101):
        ekspansja_data = ekspansja(randint(-100, 100), 1.0, 2.0, 1000)
        # Przypisz wartości do odpowiednich kolumn
        row = [ekspansja_data[0], ekspansja_data[1], ekspansja_data[2], ekspansja_data[3]]
        data.append(row)
    with open('daneCSV/daneEKSPANSJIalfa20.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

    data = [['x', 'a', 'b', 'calls']]
    for i in range(1, 101):
        ekspansja_data = ekspansja(randint(-100, 100), 1.0, 1.5, 1000)
        # Przypisz wartości do odpowiednich kolumn
        row = [ekspansja_data[0], ekspansja_data[1], ekspansja_data[2], ekspansja_data[3]]
        data.append(row)
    with open('daneCSV/daneEKSPANSJIalfa15.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)


    data = [['x', 'a', 'b', 'calls']]
    for i in range(1, 101):
        ekspansja_data = ekspansja(randint(-100, 100), 1.0, 1.2, 1000)
        # Przypisz wartości do odpowiednich kolumn
        row = [ekspansja_data[0], ekspansja_data[1], ekspansja_data[2], ekspansja_data[3]]
        data.append(row)
    with open('daneCSV/daneEKSPANSJIalfa12.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

