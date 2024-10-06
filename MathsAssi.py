from pulp import LpProblem, LpMaximize, LpVariable, lpSum, LpStatus, value, PULP_CBC_CMD


problem = LpProblem("Maximize_Profit", LpMaximize)


x_A = LpVariable('x_A', lowBound=0, cat='Integer')  
x_B = LpVariable('x_B', lowBound=0, cat='Integer')  


problem += 5 * x_A + 8 * x_B, "Total Profit"


problem += 2 * x_A + 4 * x_B <= 60, "Labour_Hours_Constraint"
problem += 3 * x_A + 2 * x_B <= 40, "Raw_Material_Constraint"


solver = PULP_CBC_CMD(msg=False)  
problem.solve(solver)


print(f"Status: {LpStatus[problem.status]}")
print(f"Units of Product A produced: {value(x_A)}")
print(f"Units of Product B produced: {value(x_B)}")
print(f"Maximum Profit: ${value(problem.objective)}")
