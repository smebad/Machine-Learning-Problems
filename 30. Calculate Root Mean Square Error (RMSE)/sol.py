# Calculate Root Mean Square Error (RMSE)
# Solution:
import numpy as np

def rmse(y_true, y_pred):
    if y_true.shape != y_pred.shape:
        raise ValueError("Arrays must have the same shape")
    if y_true.size == 0:
        raise ValueError("Arrays cannot be empty")
    return round(np.sqrt(np.mean((y_true - y_pred) ** 2)), 3)

# Test Case:
y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])
print(rmse(y_true, y_pred))  # Output: 0.612
