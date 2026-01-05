# Calculate 2x2 Matrix Inverse
# Write a Python function that calculates the inverse of a 2x2 matrix. The inverse of a matrix A is another matrix Aâ»Â¹ such that A Ã Aâ»Â¹ = I (the identity matrix).

# For a 2x2 matrix [[a, b], [c, d]], the inverse exists only if the determinant (ad - bc) is non-zero.

# Return None if the matrix is not invertible (i.e., when the determinant equals zero).

# Example:
# Input:
# matrix = [[4, 7], [2, 6]]
# Output:
# [[0.6, -0.7], [-0.2, 0.4]]
# Reasoning:
# For matrix [[a, b], [c, d]] = [[4, 7], [2, 6]]:

# Calculate determinant: det = ad - bc = 4×6 - 7×2 = 24 - 14 = 10
# Since det ≠ 0, the matrix is invertible
# Apply formula: A⁻¹ = (1/det) × [[d, -b], [-c, a]] = (1/10) × [[6, -7], [-2, 4]] = [[0.6, -0.7], [-0.2, 0.4]]


# Solution:
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    
    determinant = a * d - b * c
    
    if determinant == 0:
        return None
    
    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]
    return inverse

# Test cases:
# Test case 1
matrix1 = [[4, 7], [2, 6]]
print(inverse_2x2(matrix1))  # Output: [[0.6, -0.7], [-0.2, 0.4]]

# Test case 2
matrix2 = [[1, 2], [3, 4]]
print(inverse_2x2(matrix2))  # Output: None

# Test case 3
matrix3 = [[2, 5], [1, 3]]
print(inverse_2x2(matrix3))  # Output: [[0.4, -0.5], [-0.2, 0.6]]

# Test case 4
matrix4 = [[0, 1], [1, 0]]
print(inverse_2x2(matrix4))  # Output: [[0, 1], [1, 0]]

# Test case 5
matrix5 = [[3, 0], [0, 3]]
print(inverse_2x2(matrix5))  # Output: [[0, 0], [0, 0]]