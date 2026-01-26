# Implement Recall Metric in Binary Classification
# Solution:
import numpy as np

def recall(y_true, y_pred):
    tp = np.sum((y_true == 1) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    
    if tp + fn == 0:
        return 0.0
    
    return tp / (tp + fn)

# Test Case:
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
print(recall(y_true, y_pred))  # Output: 0.75
