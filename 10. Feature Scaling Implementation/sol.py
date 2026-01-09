# Feature Scaling Implementation
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
