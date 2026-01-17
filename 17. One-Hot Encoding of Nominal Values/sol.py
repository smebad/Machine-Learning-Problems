# One-Hot Encoding of Nominal Values
# Solution:
import numpy as np

def to_categorical(x, n_col=None):
    if not n_col:
        n_col = np.amax(x) + 1
    one_hot = np.zeros((x.shape[0], n_col))
    one_hot[np.arange(x.shape[0]), x] = 1
    return one_hot

# Test Case:
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [0. 1. 0.]
#  [1. 0. 0.]]
