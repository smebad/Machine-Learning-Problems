# Batch Iterator for Dataset
# Implement a batch iterable function that samples in a numpy array X and an optional numpy array y. The function should return batches of a specified size. If y is provided, the function should return batches of (X, y) pairs; otherwise, it should return batches of X only.

# Example:
# Input:
# X = np.array([[1, 2], 
#                   [3, 4], 
#                   [5, 6], 
#                   [7, 8], 
#                   [9, 10]])
#     y = np.array([1, 2, 3, 4, 5])
#     batch_size = 2
#     batch_iterator(X, y, batch_size)
# Output:
# [[[[1, 2], [3, 4]], [1, 2]],
#      [[[5, 6], [7, 8]], [3, 4]],
#      [[[9, 10]], [5]]]
# Reasoning:
# The dataset X contains 5 samples, and we are using a batch size of 2. Therefore, the function will divide the dataset into 3 batches. The first two batches will contain 2 samples each, and the last batch will contain the remaining sample. The corresponding values from y are also included in each batch.


# Solution:
import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    n_samples = X.shape[0]
    batches = []
    for i in np.arange(0, n_samples, batch_size):
        begin, end = i, min(i+batch_size, n_samples)
        if y is not None:
            batches.append([X[begin:end], y[begin:end]])
        else:
            batches.append( X[begin:end])
    return batches
    
# Test Case:
X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batches = batch_iterator(X, y, batch_size=2)
print(batches)
