import matplotlib.pyplot as plt
import numpy as np
import math

# Урок 3
# Задание 1.2
# Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)


def LineLengthXY(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def LineLengthXYZ(x1, x2, y1, y2, z1, z2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


print('Длина вектора составит: ' + str(LineLengthXY(
    int(input('Введите x1 вектора:')),
    int(input('Введите у1 вектора:')),
    int(input('Введите x2 вектора:')),
    int(input('Введите у2 вектора:'))
    )))



