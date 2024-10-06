import numpy as np
import matplotlib.pyplot as plt

# Define the constraint lines
# Constraint 1: 5x1 + 3x2 <= 30
# Solving for x2: x2 = (30 - 5x1) / 3
def constraint1(x1):
    return (30 - 5 * x1) / 3

# Constraint 2: x1 + 2x2 <= 18
# Solving for x2: x2 = (18 - x1) / 2
def constraint2(x1):
    return (18 - x1) / 2

# Set up the plot
x1_values = np.linspace(0, 10, 400)  # Range for x1

plt.figure(figsize=(8, 8))

# Plot the constraints
plt.plot(x1_values, constraint1(x1_values), label=r'$5x_1 + 3x_2 \leq 30$')
plt.plot(x1_values, constraint2(x1_values), label=r'$x_1 + 2x_2 \leq 18$')

# Fill the feasible region
x1 = np.linspace(0, 6, 400)
x2 = np.minimum(constraint1(x1), constraint2(x1))
plt.fill_between(x1, 0, x2, where=(x2 >= 0), color='lightblue', alpha=0.5)

# Labels and plot limits
plt.xlim(0, 10)
plt.ylim(0, 10)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

# Title and legend
plt.title('Feasible Region for the LPP')
plt.legend()

# Display the plot
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()
