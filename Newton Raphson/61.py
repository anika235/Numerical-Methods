import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x - 1

def f_of(x):
    return 3 * x**2 - 1

def newton_raphson_method(x0, max=10):
    approx_error = []
    x_values = []
    i = 0

    while i < max:
        xi = x0
        fi = f(xi)
        f_of_i = f_of(xi)

        xi_plus_1 = xi - fi / f_of_i
        error = abs(xi_plus_1 - xi)
        rel_approxerror = abs(error / xi_plus_1)

        print(f"Iteration {i+1}:")
        print(f"xi = {xi:.6f}, f(xi) = {fi:.6f}, f'(xi) = {f_of_i:.6f}")
        print(f"xi+1 = {xi_plus_1:.6f}, Approximation error = {error:.6f}, Relative approximation error = {rel_approxerror:.6f}")
        
        x_values.append(xi_plus_1)
        approx_error.append(error)

        x0 = xi_plus_1
        i += 1

    return x_values, approx_error

x0 = 50

x_values, approx_error = newton_raphson_method(x0)

iterations = list(range(1, len(approx_error) + 1))
plt.bar(iterations, approx_error)
plt.xlabel('Iteration Number')
plt.ylabel('Approximation Error')
plt.title('Approximation Errors using Newton-Raphson Method')
plt.show()
