# Convert Vector to Diagonal Matrix
# Solution:
import numpy as np
def make_diagonal(x):
    identity_matrix = np.identity(np.size(x))
    return (identity_matrix*x)

# Test cases
x = np.array([1, 2, 3])
output = make_diagonal(x)
print(output)
