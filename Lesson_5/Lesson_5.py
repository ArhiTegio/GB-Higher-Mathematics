#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import itertools
from sklearn import datasets
import math
from functools import reduce

# 1. Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).
roulette = [0 for p in range(0, 37)]
m = 10000
for n, i in enumerate(range(0, m), start=1):
    roulette[int(round(np.random.uniform(0, 36), 0))] += 1

print([p / m for p in roulette])

dict = {n: p for n, p in enumerate(roulette)}
print(dict)

X = np.arange(len(dict))
plt.bar(X, dict.values(), align='center', width=1.0)
plt.xticks(X, dict.keys())
ymax = max(dict.values()) + 1
plt.ylim(0, ymax)
plt.show()


#2.1-----------------------------------------------------------------------
#Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере рулетки или подбрасывания монетки.
# roulette = [0 for p in range(0, 37)]
# m = 100000
# for _ in range(0, m):
#     roulette[int(round(np.random.uniform(0, 36), 0))] += 1
#
# probabilitys = [n / m for n in roulette]
# print(probabilitys)
#
# x1 = 0
# x2 = 3
# probability = sum([probabilitys[p] for p in range(x1, x2)])
# cheak = 0
#
# list = [p for p in range(x1, x2)]
# for _ in range(0, m):
#     pos = int(round(np.random.uniform(0, 36), 0))
#     if pos in list:
#         cheak += 1
#
# print("Проверка теории сложения вероятности при " + str(m) + " подходов. Составит для полей " +
#       ", ".join([str(p) for p in range(x1, x2)]) + ": " + str(probability) + " = " + str(cheak / m))
#


#2.2-----------------------------------------------------------------------
#Сгенерируйте десять выборок случайных чисел х0, …, х9.
#и постройте гистограмму распределения случайной суммы х0+х1+ …+ х9.
# dict = {str("x" + str(n)): p for n, p in enumerate([sum(np.random.rand(10)) for p in range(0, 10)])}
# print(dict)
#
# X = np.arange(len(dict))
# plt.bar(X, dict.values(), align='center', width=0.5)
# plt.xticks(X, dict.keys())
# ymax = max(dict.values()) + 1
# plt.ylim(0, ymax)
# plt.show()


#3.1 Дополните код Монте-Карло последовательности независимых испытаний расчетом соответствующих вероятностей (через биномиальное распределение) и сравните результаты.
#3.2 Повторите расчеты биномиальных коэффициентов и вероятностей k успехов в последовательности из n независимых испытаний, взяв другие значения n и k.
# p = 0.5
# k = 2 # Количество успехов
# n = 4 # Количество испытаний
# m = 10000
# x = np.random.randint(0, k, m)
# for _ in range(1, n):
#     x += np.random.randint(0, k, m)
# print('k = ' + str(k))
# print('n = ' + str(n))
# print('p = ' + str(p))
# print('q = 1 - ' + str(p) + ' = ' + str(1 - p))
# print(str(1 - p))
# print(str(n - k))
# print('P' + str(n) + '(' + str(k) + ') = ' + str(math.factorial(n)/(math.factorial(k) * math.factorial(n - k))) +
#       ' · ' + str(p ** k) + ' · ' + str((1 - p) ** (n - k)) + ' = ' +
#       str((math.factorial(n)/(math.factorial(k) * math.factorial(n - k))) * (p ** k) * ((1 - p) ** (n - k))))
# k1 = 0
# for i in range(0, m):
#     if x[i] == 2:
#         k1 += 1
# print(k1, n, k1/m)

# 4 Из урока по комбинаторике повторите расчеты, сгенерировав возможные варианты перестановок для других значений n и k
# n = 8
# k = 3
# num = 0
#
# for p in itertools.permutations(''.join([str(p) for p in range(0, n)]), k):
#     print(''.join(str(x) for x in p))
#     num += 1
#
# print('Количество: ' + str(num))
# print('Размещение (сколько комбинаций чисел из n символов можно разместить с учетом растоновки в k символах): ' +
#       str(math.factorial(n)/(math.factorial(n - k))))

# 5 Дополните код расчетом коэффициента корреляции x и y по формуле
n = 100
r = 0.7
x = np.random.rand(n)
y = r * x + (1 - r) * np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
c = np.corrcoef(x, y)
print(c)

a = (np.sum(x) * np.sum(y) - n * np.sum(x * y)) / (np.sum(x) * np.sum(x) - n * np.sum(x * x))
b = (np.sum(y) - a * np.sum(x)) / n
x_average = np.sum(x) / len(x)
y_average = np.sum(y) / len(y)
print(x_average)
print(y_average)
xy = zip(x, y)
print('---- Коэффициент корреляции Пирсона')
v1 = sum([(x1 - x_average) * (y1 - y_average) for x1, y1 in xy])
v2 = sum([(x1 - x_average) ** 2 for x1 in x])
v3 = sum([(y1 - y_average) ** 2 for y1 in y])
R = round(v1 / ((v2 * v3) ** (1/2)), 2)
print('R = ' + str(R))
if 0.9 < abs(R):
    print('Связь функциональная')
if 0.7 < abs(R) <= 0.9:
    print('Связь сильная')
if 0.5 < abs(R) <= 0.7:
    print('Связь умеренная')
if 0.3 < abs(R) <= 0.5:
    print('Связь слабая')
if 0.0 < abs(R) <= 0.3:
    print('Связь минимальная')
if abs(R) == 0:
    print('Связь отсутствует')
print('----')

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
plt.plot([0, 1], [b, a + b])
plt.show()

