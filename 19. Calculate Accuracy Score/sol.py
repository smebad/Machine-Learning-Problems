# Calculate Accuracy Score
# Write a Python function to calculate the accuracy score of a model's predictions. The function should take in two 1D numpy arrays: y_true, which contains the true labels, and y_pred, which contains the predicted labels. It should return the accuracy score as a float.

# Example:
# Input:
# y_true = np.array([1, 0, 1, 1, 0, 1])
#     y_pred = np.array([1, 0, 0, 1, 0, 1])
#     output = accuracy_score(y_true, y_pred)
#     print(output)
# Output:
# # 0.8333333333333334
# Reasoning:
# The function compares the true labels with the predicted labels and calculates the ratio of correct predictions to the total number of predictions. In this example, there are 5 correct predictions out of 6, resulting in an accuracy score of 0.8333333333333334.


# Solution:
import numpy as np

def accuracy_score(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred, axis=0) / len(y_true)
    return accuracy

# Test cases
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)
print(output)  # Output: 0.8333333333333334