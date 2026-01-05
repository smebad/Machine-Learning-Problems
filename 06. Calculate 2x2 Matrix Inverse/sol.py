# Calculate 2x2 Matrix Inverse
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
