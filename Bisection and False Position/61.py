# -*- coding: utf-8 -*-
"""61

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12QVoHg7Bx7e5HjYA5RbBazPaAOds6ime
"""

import matplotlib.pyplot as plt
import numpy as np

# Given function
def f(x):
    return x**3 - x - 1

# Bisection method
def bisection(a, b, tol, max_iter):
    x_vals = []
    approx_errors = []
    relative_approx_errors = []

    for i in range(max_iter):
        c = (a + b) / 2
        x_vals.append(c)

        if i>0:
          approx_error = abs(x_vals[i] - x_vals[i - 1]) / 2
          relative_approx_error = approx_error  / abs(x_vals[i])
          approx_errors.append(approx_error)
          relative_approx_errors.append(relative_approx_error)

          if approx_error < tol:
              break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return x_vals, approx_errors, relative_approx_errors

# False Position method
def false_position(a, b, tol, max_iter):
    x_vals = []
    approx_errors = []
    relative_approx_errors = []

    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        x_vals.append(c)

        if i>0:
          approx_error = abs(x_vals[i] - x_vals[i - 1]) / 2
          relative_approx_error = approx_error  / abs(x_vals[i])
          approx_errors.append(approx_error)
          relative_approx_errors.append(relative_approx_error)

          if  approx_error < tol:
              break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, approx_errors, relative_approx_errors

# Initial values
x0 = 50
x1 = -50
tolerance = 1e-6
max_iterations = 1000

# Bisection method
root_bisection, approx_errors_bisection, relative_approx_errors_bisection = bisection(x0, x1, tolerance, max_iterations)

# False Position method
root_false_position, approx_errors_false_position, relative_approx_errors_false_position = false_position(x0, x1, tolerance, max_iterations)

# Plotting bar charts
iterations = np.arange(1, len(approx_errors_bisection) + 1)
iteration_numbers_false = np.arange(1, len(approx_errors_false_position)+1)


plt.bar(iterations, approx_errors_bisection, label='Bisection')
plt.xlabel('Iteration')
plt.ylabel('Approximation Error')
plt.legend()
plt.title('Approximation Errors vs Iteration Number')
plt.show()

plt.bar(iterations, relative_approx_errors_bisection, label='Bisection')

plt.xlabel('Iteration')
plt.ylabel('Relative Approximation Error')
plt.legend()
plt.title('Relative Approximation Errors vs Iteration Number')
plt.show()


plt.bar(iteration_numbers_false, approx_errors_false_position, label='False Position')
plt.xlabel('Iteration Number')
plt.ylabel('Approximation Error')
plt.title('Approximation Error vs Iteration Number(False)')
plt.legend()
plt.show()

plt.bar(iteration_numbers_false, relative_approx_errors_false_position, label='False Position')
plt.xlabel('Iteration Number')
plt.ylabel('Approximation Error')
plt.title('Relative Approximation Error vs Iteration Number(False)')
plt.legend()
plt.show()

# Line Chart for Relative Approximation Errors
plt.plot(iterations, approx_errors_bisection, marker='o', label='Bisection')
plt.plot(iteration_numbers_false, approx_errors_false_position, marker='o',  label='False Position')
plt.xlabel('Iteration Number')
plt.ylabel('Approximation Error')
plt.title('Approximation Error vs Iteration Number')
plt.legend()
plt.show()


# Line Chart for Relative Approximation Errors
plt.plot(iterations, relative_approx_errors_bisection , marker='o',  label='Bisection')
plt.plot(iteration_numbers_false,relative_approx_errors_false_position , marker='o', label='False Position')
plt.xlabel('Iteration Number')
plt.ylabel('Relative Approximation Error')
plt.title('Relative Approximation Error vs Iteration Number')
plt.legend()
plt.show()