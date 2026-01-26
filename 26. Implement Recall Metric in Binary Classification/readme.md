# Implement Recall Metric in Binary Classification

## 1. What is Recall and Why It Matters

Recall is a performance metric used in binary classification to measure how well a model finds all the positive cases. It answers the question: out of all the actual positive samples, how many did the model correctly identify as positive.

Mathematically, recall is defined as:

Recall = True Positives / (True Positives + False Negatives)

* True Positives (TP): cases where the model correctly predicted a positive label.
* False Negatives (FN): cases where the model predicted negative but the actual label was positive.

Recall is especially important in problems where missing a positive case is costly. For example, in medical diagnosis, failing to detect a disease is more serious than raising a false alarm.

---

## 2. Problem Description

You are given two arrays:

* y_true: the actual binary labels.
* y_pred: the predicted binary labels.

Your task is to compute the recall score. If there are no actual positive samples (TP + FN = 0), the function should return 0.0 to avoid division by zero.

---

## 3. Solution with Comments

```python
import numpy as np

def recall(y_true, y_pred):
    # Count True Positives: cases where both actual and predicted labels are 1
    tp = np.sum((y_true == 1) & (y_pred == 1))
    
    # Count False Negatives: actual label is 1 but predicted label is 0
    fn = np.sum((y_true == 1) & (y_pred == 0))
    
    # If there are no actual positive cases, return 0.0 to avoid division by zero
    if tp + fn == 0:
        return 0.0
    
    # Recall formula
    return tp / (tp + fn)

# Test Case
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
print(recall(y_true, y_pred))  # Output: 0.75
```

---

## 4. How the Solution Works

The function first identifies which predictions are true positives and which are false negatives using NumPy logical operations. By comparing y_true and y_pred element by element, it counts how many times the model correctly predicted a positive (TP) and how many times it missed a positive (FN).

Once TP and FN are known, the recall formula is applied. If there are no actual positives, recall is defined as 0.0 to avoid dividing by zero.

---

## 5. Step by Step Example

For the input:

* y_true = [1, 0, 1, 1, 0, 1]
* y_pred = [1, 0, 1, 0, 0, 1]

Actual positive labels (1s) appear 4 times in y_true. The model correctly predicted 3 of them as positive. Therefore:

Recall = 3 / 4 = 0.75

---

## 6. Understanding the Logic in Simple Terms

Recall tells us how many of the real positive cases were found by the model. If recall is high, it means the model is good at catching positives and not missing them. If recall is low, the model is failing to identify many positive cases.

This implementation is efficient because it uses NumPy operations instead of manual loops, making it fast and easy to read. It also safely handles edge cases where there are no positive examples.

---

## 7. Key Takeaway


Recall is a crucial metric when missing positive cases is risky. This implementation correctly computes recall by counting true positives and false negatives and applying the standard formula in a safe and reliable way.
