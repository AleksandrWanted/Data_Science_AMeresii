import numpy as np


"""Задание 1:

Используя офисное приложение или текстовый редактор
подготовить данные в формате .csv

Ответ: файл rand_matrix.csv

"""


"""Задание 2:

Прочитать эти данные в numpy

"""

matrix = np.loadtxt(delimiter=",", fname='rand_matrix.csv')
print('Матрица полученная из файла rand_matrix.csv:\n%s' % matrix)


"""Задание 3:

Найти максимум и минимум и поменять их местами

"""

matrix_max = np.max(matrix)
matrix_min = np.min(matrix)

print("максимум - %s" % matrix_max)
print("минимум - %s" % matrix_min)

r_max = np.where(matrix == matrix_max)
r_min = np.where(matrix == matrix_min)

matrix[r_max[0], r_max[1]] = matrix_min
matrix[r_min[0], r_min[1]] = matrix_max

print('Матрица после замены max<>min:\n%s' % matrix)
