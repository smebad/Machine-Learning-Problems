# Scalar Multiplication of a Matrix
# Write a Python function that multiplies a matrix by a scalar and returns the result.

# Example:
# Input:
# matrix = [[1, 2], [3, 4]], scalar = 2
# Output:
# [[2, 4], [6, 8]]
# Reasoning:
# Each element of the matrix is multiplied by the scalar.



# Solution:
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    return [[element * scalar for element in row] for row in matrix]


# Test cases
if __name__ == "__main__":
    # Test case 1
    matrix = [[1, 2], [3, 4]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[2, 4], [6, 8]]

    # Test case 2
    matrix = [[0, -1], [5, 3]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[0, -2], [10, 6]]

    # Test case 3
    matrix = [[1.5, 2.5], [3.5, 4.5]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[3.0, 5.0], [7.0, 9.0]]

    # Test case 4
    matrix = [[-1, -2], [-3, -4]]
    scalar = 2
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[2, 4], [6, 8]]

    # Test case 5
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    scalar = 3
    result = scalar_multiply(matrix, scalar)
    print(result)  # Output: [[3, 6, 9], [12, 15, 18], [21, 24, 27]]