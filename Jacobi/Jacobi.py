# -*- coding: utf-8 -*-
"""61.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fulAEBv_YHggTy0eQrHixOR_et1zHX-
"""

import numpy as np
import matplotlib.pyplot as plt
import time as tm
import tabulate

def input_matrix(prompt, dimension):
    matrix = np.zeros((dimension, dimension))
    for i in range(dimension):
        for j in range(dimension):
            matrix[i][j] = float(input(prompt.format(i+1, j+1)))
    return matrix

def input_vector(prompt, dimension):
    vector = np.zeros(dimension)
    for i in range(dimension):
        vector[i] = float(input(prompt.format(i+1)))
    return vector

dimension = int(input("Enter the dimension of the system: "))
coeff_matrix = input_matrix("Enter coefficient for row {}, column {}: ", dimension)
const_vector = input_vector("Enter constant for equation {}: ", dimension)

x0 = np.zeros(dimension)

D = np.diag(np.diag(coeff_matrix))
L_plus_U = coeff_matrix - D
C = np.matmul(np.linalg.inv(D), const_vector)
T = -np.matmul(np.linalg.inv(D), L_plus_U)

jacobi_iteration_array = []
time_iter = []
time_matr = []

def check_solution(x):
    ans = np.matmul(coeff_matrix, x) - const_vector
    return all(abs(i) <= 1e-5 for i in ans)

def jacobi_iteration(x):
    return np.matmul(T, x) + C

def jacobi_matrixless_iteration(x):
    x_k = []
    for i in range(dimension):
        x_k_i = (const_vector[i] - np.dot(coeff_matrix[i], x) + coeff_matrix[i, i] * x[i]) / coeff_matrix[i, i]
        x_k.append(x_k_i)
    return x_k

while not check_solution(x0):
    x0 = jacobi_matrixless_iteration(x0)
    jacobi_iteration_array.append(x0)
    time_iter.append(tm.time())

x0 = np.zeros(dimension)
while not check_solution(x0):
    x0 = jacobi_iteration(x0)
    time_matr.append(tm.time())

approx_error = [np.abs(np.array(jacobi_iteration_array[i]) - np.array(jacobi_iteration_array[i-1])) for i in range(1, len(jacobi_iteration_array))]
time_iter = [(t - time_iter[0]) * 1e6 for t in time_iter]
time_matr = [(t - time_matr[0]) * 1e6 for t in time_matr]

print("Values of x")
headers = [f'x{i+1}' for i in range(dimension)]
print(tabulate.tabulate(jacobi_iteration_array, headers=headers, tablefmt='orgtbl'))

print("Approximation errors")
print(tabulate.tabulate(approx_error, headers=headers, tablefmt='orgtbl'))

plt.plot(range(len(approx_error)), [sum(err) for err in approx_error], marker='o')
plt.title('Total Approximation Errors')
plt.xlabel('Iteration')
plt.ylabel('Approximation error')
plt.show()

plt.plot(range(len(time_iter)), time_iter, marker='o', label='Matrix-less Jacobi')
plt.legend()
plt.title('Cumulative Runtimes')
plt.xlabel('Iteration')
plt.ylabel('Cumulative Runtimes')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import time as tm
import tabulate

def input_matrix(prompt, dimension):
    matrix = np.zeros((dimension, dimension))
    for i in range(dimension):
        for j in range(dimension):
            matrix[i][j] = float(input(prompt.format(i+1, j+1)))
    return matrix

def input_vector(prompt, dimension):
    vector = np.zeros(dimension)
    for i in range(dimension):
        vector[i] = float(input(prompt.format(i+1)))
    return vector

dimension = int(input("Enter the dimension of the system: "))
coeff_matrix = input_matrix("Enter coefficient for row {}, column {}: ", dimension)
const_vector = input_vector("Enter constant for equation {}: ", dimension)

x0 = np.zeros(dimension)

D = np.diag(np.diag(coeff_matrix))
L_plus_U = coeff_matrix - D
C = np.matmul(np.linalg.inv(D), const_vector)
T = -np.matmul(np.linalg.inv(D), L_plus_U)

jacobi_iteration_array = []
time_iter = []
time_matr = []

def check_solution(x):
    ans = np.matmul(coeff_matrix, x) - const_vector
    return all(abs(i) <= 1e-5 for i in ans)

def jacobi_iteration(x):
    return np.matmul(T, x) + C

def jacobi_matrixless_iteration(x):
    x_k = []
    for i in range(dimension):
        x_k_i = (const_vector[i] - np.dot(coeff_matrix[i], x) + coeff_matrix[i, i] * x[i]) / coeff_matrix[i, i]
        x_k.append(x_k_i)
    return x_k

while not check_solution(x0):
    x0 = jacobi_matrixless_iteration(x0)
    jacobi_iteration_array.append(x0)
    time_iter.append(tm.time())

x0 = np.zeros(dimension)
while not check_solution(x0):
    x0 = jacobi_iteration(x0)
    time_matr.append(tm.time())

approx_error = [np.abs(np.array(jacobi_iteration_array[i]) - np.array(jacobi_iteration_array[i-1])) for i in range(1, len(jacobi_iteration_array))]
time_iter = [(t - time_iter[0]) * 1e6 for t in time_iter]
time_matr = [(t - time_matr[0]) * 1e6 for t in time_matr]

print("Approximation errors")
print(tabulate.tabulate(approx_error, headers=headers))

plt.plot(range(len(time_iter)), time_iter, marker='o', label='Matrix-less Jacobi')
plt.plot(range(len(time_matr)), time_matr, marker='o', label='Matrix-based Jacobi')
plt.legend()
plt.title('Cumulative Runtimes')
plt.xlabel('Iteration')
plt.ylabel('Cumulative Runtimes')
plt.show()