# Transformation Matrix from Basis B to C
# Solution:
import numpy as np

def transform_basis(B, C):
    C = np.array(C)
    B = np.array(B)
    C_inv = np.linalg.inv(C)
    P = np.dot(C_inv, B)
    return P.tolist()

# Test Case:
B = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
C = [[1, 2.3, 3], [4.4, 25, 6], [7.4, 8, 9]]
print(transform_basis(B, C)) # Expected Output: [[-0.6772, -0.0126, 0.2342], [-0.0184, 0.0505, -0.0275], [0.5732, -0.0345, -0.0569]]
