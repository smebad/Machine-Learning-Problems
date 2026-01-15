# Random Shuffle of Dataset
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
