# Implement Precision Metric
# Solution:
import numpy as np

def precision(y_true, y_pred):
    true_positives = np.sum((y_true == 1) & (y_pred == 1))
    false_positives = np.sum((y_true == 0) & (y_pred == 1))
    return true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0.0

# Test Case:
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
result = precision(y_true, y_pred)
print(result)  # Output: 1.0
