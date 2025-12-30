# Matrix Vector Dot Product
# Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

# Example:
# Input:
# a = [[1, 2], [2, 4]], b = [1, 2]
# Output:
# [5, 10]
# Reasoning:
# Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (2 * 1) + (4 * 2) = 2 + 8 = 10

# Solution:
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if len(a[0]) != len(b):
        return -1
    result = []
    for row in a:
        total = 0
        for i in range(len(row)):
            total += row[i] * b[i]
        result.append(total)
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    a = [[1, 2], [2, 4]]
    b = [1, 2]
    print(matrix_dot_vector(a, b))  # Output: [5, 10]

    # Test case 2
    a = [[1, 0, 2], [0, 3, -1], [4, 1, 0]]
    b = [3, 5, 2]
    print(matrix_dot_vector(a, b))  # Output: [7, 13, 17]

    # Test case 3
    a = [[1, 2, 3], [4, 5, 6]]
    b = [7, 8]
    print(matrix_dot_vector(a, b))  # Output: -1 (incompatible dimensions)

    # Test case 4
    a = [[0, -1], [1, 0]]
    b = [2, 3]
    print(matrix_dot_vector(a, b))  # Output: [-3, 2]