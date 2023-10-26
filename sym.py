import numpy as np
import matplotlib.pyplot as plt

# Заданные параметры
PA = 0.7  # м^2
VA0 = 5  # м^3
TA0 = 90  # °C
PB = 1  # м^2
VB0 = 1  # м^3
TB0 = 10  # °C
T_in = 10  # °C
FB_in = 10 / 1000  # л/с в м^3/с
DB = 36.5665  # см^2 в м^2
a = 0.98
b = 0.63
g = 9.81  # м/с^2

# Задаем параметры для оптимизации
t_start = 0
t_end = 1000
dt = 1
target_temp = 50

# Инициализация переменных
DA0 = 1  # начальное значение DA
DA1 = 100  # конечное значение DA
epsilon = 0.01  # точность

# Метод Фибоначчи для оптимизации
def fibonacci_search(a, b, target_temp):
    # Генерируем ряд чисел Фибоначчи
    fib_sequence = [1, 1]
    while fib_sequence[-1] < (b-a)/epsilon:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    n = len(fib_sequence) - 2
    x1 = a + (b-a) * (fib_sequence[n-2] / fib_sequence[n])
    x2 = a + (b-a) * (fib_sequence[n-1] / fib_sequence[n])
    f1 = simulate(x1, target_temp)
    f2 = simulate(x2, target_temp)
    
    for k in range(n-2):
        if f1 < f2:
            b = x2
            x2 = x1
            x1 = a + (b-a) * (fib_sequence[n-k-3] / fib_sequence[n-k-1])
            f2 = f1
            f1 = simulate(x1, target_temp)
        else:
            a = x1
            x1 = x2
            x2 = a + (b-a) * (fib_sequence[n-k-2] / fib_sequence[n-k-1])
            f1 = f2
            f2 = simulate(x2, target_temp)
    return (a + b) / 2

# Функция для симуляции
def simulate(DA, target_temp):
    V = VB0
    T = TB0
    t = t_start
    while t <= t_end:
        dVdt = -a * b * DA * np.sqrt(2 * g * V / PB)
        V += dVdt * dt
        
        dTdt = (VA0 * TA0 + VB0 * T_in - V * T) / V
        T += dTdt * dt
        
        if T >= target_temp:
            return T
        t += dt
    return T

# Оптимизация
optimized_DA = fibonacci_search(DA0, DA1, target_temp)
print(f'Оптимальное значение DA: {optimized_DA} см^2')

# Симуляция с оптимальным DA
V = VB0
T = TB0
t = t_start
time_points = [t]
temperature_points = [T]
while t <= t_end:
    dVdt = -a * b * optimized_DA * np.sqrt(2 * g * V / PB)
    V += dVdt * dt
    
    dTdt = (VA0 * TA0 + VB0 * T_in - V * T) / V
    T += dTdt * dt
    
    time_points.append(t)
    temperature_points.append(T)
    t += dt

# Сохранение результатов в файл
with open('results.txt', 'w') as file:
    for t, T in zip(time_points, temperature_points):
        file.write(f'{t}\t{T}\n')

# Построение графика
plt.plot(time_points, temperature_points)
plt.xlabel('Время (с)')
plt.ylabel('Температура (°C)')
plt.title('Изменение температуры в зборнике B')
plt.show()
