# Transpose of a Matrix
# Write a Python function that computes the transpose of a given 2D matrix. The transpose of a matrix is formed by turning its rows into columns and columns into rows. For an mÃn matrix, the transpose will be an nÃm matrix.

# Example:
# Input:
# a = [[1, 2, 3], [4, 5, 6]]
# Output:
# [[1, 4], [2, 5], [3, 6]]
# Reasoning:
# The input is a 2×3 matrix. The transpose swaps rows and columns: the first row [1, 2, 3] becomes the first column, and the second row [4, 5, 6] becomes the second column, resulting in a 3×2 matrix.

# Solution:
def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    return [list(row) for row in zip(*a)]


# Test cases
if __name__ == "__main__":
    # Test case 1
    a = [[1, 2, 3], [4, 5, 6]]
    print(transpose_matrix(a))  # Expected output: [[1, 4], [2, 5], [3, 6]]

    # Test case 2
    b = [[7, 8], [9, 10], [11, 12]]
    print(transpose_matrix(b))  # Expected output: [[7, 9, 11], [8, 10, 12]]

    # Test case 3
    c = [[1]]
    print(transpose_matrix(c))  # Expected output: [[1]]

    # Test case 4
    d = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(transpose_matrix(d))  # Expected output: [[1, 3, 5, 7], [2, 4, 6, 8]]