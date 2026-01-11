# Softmax Activation Function Implementation
# Solution:

import math
def softmax(scores: list[float]) -> list[float]:
    exp_scores = [math.exp(score) for score in scores]
    sum_exp_scores = sum(exp_scores)
    probabilities = [round(score / sum_exp_scores, 4) for score in exp_scores]
    return probabilities

# Test Case
# Test Case 1:
scores = [1, 2, 3]
print(softmax(scores))  # Output: [0.0900, 0.2447, 0.6652]

# Test Case 2:
scores = [5, 10, 15]
print(softmax(scores))  # Output: [0.0000, 0.0067, 0.9933]

# Test Case 3:
scores = [0, 0, 0]
print(softmax(scores))  # Output: [0.3333, 0.3333, 0.3333]
