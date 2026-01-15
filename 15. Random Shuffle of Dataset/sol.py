# Random Shuffle of Dataset
# Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them. The function should have an optional seed parameter for reproducibility.

# Example:
# Input:
# X = np.array([[1, 2], 
#                   [3, 4], 
#                   [5, 6], 
#                   [7, 8]])
#     y = np.array([1, 2, 3, 4])
# Output:
# (array([[5, 6],
#                     [1, 2],
#                     [7, 8],
#                     [3, 4]]), 
#              array([3, 1, 4, 2]))
# Reasoning:
# The samples in X and y are shuffled randomly, maintaining the correspondence between the samples in both arrays.


# Solution:
import numpy as np

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]
    
# Test Case:
X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]])
y = np.array([1, 2, 3, 4])
shuffled_X, shuffled_y = shuffle_data(X, y, seed=42)
print(shuffled_X)
print(shuffled_y)
