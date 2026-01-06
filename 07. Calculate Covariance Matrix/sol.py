# Calculate Covariance Matrix
# Write a Python function to calculate the covariance matrix for a given set of vectors. The function should take a list of lists, where each inner list represents a feature with its observations, and return a covariance matrix as a list of lists. Additionally, provide test cases to verify the correctness of your implementation.

# Example:
# Input:
# [[1, 2, 3], [4, 5, 6]]
# Output:
# [[1.0, 1.0], [1.0, 1.0]]
# Reasoning:
# The covariance between the two features is calculated based on their deviations from the mean. For the given vectors, both covariances are 1.0, resulting in a symmetric covariance matrix.


# Solution:
import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n_features = len(vectors)
    n_observations = len(vectors[0])
    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)]

    means = [sum(feature) / n_observations for feature in vectors]

    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(n_observations)) / (n_observations - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

    return covariance_matrix

# Test cases
def test_calculate_covariance_matrix():
    # Test case 1
    vectors = [[1, 2, 3], [4, 5, 6]]
    expected = [[1.0, 1.0], [1.0, 1.0]]
    assert calculate_covariance_matrix(vectors) == expected
    
    # Test case 2
    vectors = [[1, 2, 3, 4], [2, 3, 4, 5], [5, 6, 7, 8]]
    expected = [[1.6666666666666667, 1.6666666666666667, 1.666666666666667],
                [1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0]]
    assert calculate_covariance_matrix(vectors) == expected
    
    # Test case 3
    vectors = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]
    expected = [[100.0, 100.0, 100.0],
                [100.0, 100.0, 100.0],
                [100.0, 100.0, 100.0]]
    assert calculate_covariance_matrix(vectors) == expected