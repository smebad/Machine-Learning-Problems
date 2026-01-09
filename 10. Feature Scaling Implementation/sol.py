# Feature Scaling Implementation
# Write a Python function that performs feature scaling on a dataset using both standardization and min-max normalization. The function should take a 2D NumPy array as input, where each row represents a data sample and each column represents a feature. It should return two 2D NumPy arrays: one scaled by standardization and one by min-max normalization. Make sure all results are rounded to the nearest 4th decimal.

# Example:
# Input:
# data = np.array([[1, 2], [3, 4], [5, 6]])
# Output:
# ([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])
# Reasoning:
# Standardization rescales the feature to have a mean of 0 and a standard deviation of 1. Min-max normalization rescales the feature to a range of [0, 1], where the minimum feature value maps to 0 and the maximum to 1.


# Solution:
import numpy as np

def feature_scaling(data):
    
    # Standardization
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std
    
    # Min-Max scaling
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)
    
    return np.round(standardized_data,4).tolist(), np.round(normalized_data,4).tolist()


# Test Case
data = np.array([[1, 2], [3, 4], [5, 6]])
standardized, normalized = feature_scaling(data)
print(standardized)  # Expected: [[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]]
print(normalized)    # Expected: [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]]
