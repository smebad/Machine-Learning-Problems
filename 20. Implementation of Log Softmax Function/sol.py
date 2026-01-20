# Implementation of Log Softmax Function
# Solution:
import numpy as np

def log_softmax(scores: list) -> np.ndarray:
    scores = scores - np.max(scores)
    return scores - np.log(np.sum(np.exp(scores)))

# Test Case:
A = np.array([1, 2, 3])
print(log_softmax(A))  # Output: array([-2.4076, -1.4076, -0.4076])
