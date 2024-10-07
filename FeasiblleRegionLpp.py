import numpy as np
from scipy.optimize import minimize

def objective_func_example1(X):
    x, y = X
    return x**2 + y**2

def constraint1_example1(X):
    return 4 - (X[0] + 2*X[1])

def constraint2_example1(X):
    return X[0] - 1

constraints1 = [{'type': 'ineq', 'fun': constraint1_example1},
                 {'type': 'ineq', 'fun': constraint2_example1}]

initial_guess1 = [0, 0]
solution1 = minimize(objective_func_example1, initial_guess1, constraints=constraints1)

def objective_func_example2(X):
    x, y = X
    return (x - 1)**2 + (y - 2)**2

def constraint1_example2(X):
    return 2 - X[0]**2 - X[1]

def constraint2_example2(X):
    return X[0] + X[1] - 4

constraints2 = [{'type': 'ineq', 'fun': constraint1_example2},
                 {'type': 'ineq', 'fun': constraint2_example2}]

initial_guess2 = [1, 1]
solution2 = minimize(objective_func_example2, initial_guess2, constraints=constraints2)

print("Example 1: Lagrange Multiplier Method Solution")
print("x:", round(solution1.x[0], 3), "y:", round(solution1.x[1], 3))
print("Objective Function Value:", round(solution1.fun, 3))

print("\nExample 1: KKT Conditions Solution")
print("x:", round(solution1.x[0], 3), "y:", round(solution1.x[1], 3))
print("Objective Function Value:", round(solution1.fun, 3))

print("\nExample 2: Lagrange Multiplier Method Solution")
print("x:", round(solution2.x[0], 3), "y:", round(solution2.x[1], 3))
print("Objective Function Value:", round(solution2.fun, 3))

print("\nExample 2: KKT Conditions Solution")
print("x:", round(solution2.x[0], 3), "y:", round(solution2.x[1], 3))
print("Objective Function Value:", round(solution2.fun, 3))
