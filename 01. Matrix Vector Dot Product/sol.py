# Matrix Vector Dot Product
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
