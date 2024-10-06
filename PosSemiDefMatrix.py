import numpy as np

def is_positive_semi_definite(matrix):
    eigenvalues = np.linalg.eigvals(matrix)
    return np.all(eigenvalues >= 0)

r= int(input("Enter the number of rows: "))
matrix = [list(map(int,input().split())) for _ in range(r)]

matrix = np.array(matrix)
result = is_positive_semi_definite(matrix)
if result:
    print("It is a positive semi-definite matrix")
else:
    print("Not a positive semi-definite matrix")
