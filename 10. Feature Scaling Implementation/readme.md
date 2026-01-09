# Feature Scaling Implementation

## 1. Problem Overview

### What is Feature Scaling?

Feature scaling is a data preprocessing technique used in machine learning to bring all features to a similar scale. Many machine learning algorithms rely on distance calculations or gradient-based optimization, and unscaled features can negatively impact their performance and convergence speed.

This problem focuses on implementing two commonly used feature scaling techniques:

* **Standardization (Z-score normalization)**
* **Min-Max normalization**

### The Problem

Write a Python function that:

* Takes a 2D NumPy array where rows represent samples and columns represent features
* Applies standardization and min-max normalization independently to each feature
* Returns both scaled datasets rounded to four decimal places

---

## 2. Code Explanation (With Comments)

```python
import numpy as np

def feature_scaling(data):
    
    # Compute mean of each feature (column-wise)
    mean = np.mean(data, axis=0)

    # Compute standard deviation of each feature
    std = np.std(data, axis=0)

    # Apply standardization: (x - mean) / std
    standardized_data = (data - mean) / std
    
    # Compute minimum value of each feature
    min_val = np.min(data, axis=0)

    # Compute maximum value of each feature
    max_val = np.max(data, axis=0)

    # Apply min-max normalization: (x - min) / (max - min)
    normalized_data = (data - min_val) / (max_val - min_val)
    
    # Round results to 4 decimal places and return as Python lists
    return np.round(standardized_data, 4).tolist(), np.round(normalized_data, 4).tolist()
```

### Key Points to Remember

* `axis=0` ensures operations are applied feature-wise.
* Standardization centers data around zero with unit variance.
* Min-max normalization scales values to the range [0, 1].
* Rounding helps avoid floating-point precision issues.

---

## 3. Solution Approach and Logic

### Step 1: Standardization

Standardization transforms each feature so that it has:

* Mean = 0
* Standard deviation = 1

Formula:

```
(x - mean) / standard deviation
```

This method is commonly used in algorithms such as linear regression, logistic regression, and support vector machines.

---

### Step 2: Min-Max Normalization

Min-max normalization rescales each feature to a fixed range, typically [0, 1].

Formula:

```
(x - min) / (max - min)
```

This method is often used when feature bounds are important, such as in neural networks or image processing.

---

## 4. Example Walkthrough

### Input

```python
data = np.array([[1, 2], [3, 4], [5, 6]])
```

### Standardization Output

```python
[[-1.2247, -1.2247],
 [ 0.0000,  0.0000],
 [ 1.2247,  1.2247]]
```

### Min-Max Normalization Output

```python
[[0.0, 0.0],
 [0.5, 0.5],
 [1.0, 1.0]]
```

---

## 5. Differences Between Standardization and Min-Max Scaling

| Aspect                | Standardization | Min-Max Normalization |
| --------------------- | --------------- | --------------------- |
| Output Range          | Unbounded       | [0, 1]                |
| Mean                  | 0               | Not fixed             |
| Standard Deviation    | 1               | Not fixed             |
| Sensitive to Outliers | Yes             | Yes                   |
| Common Use            | Regression, SVM | Neural Networks       |

---

## 6. Test Case
```python
# Test Case
data = np.array([[1, 2], [3, 4], [5, 6]])
standardized, normalized = feature_scaling(data)
print(standardized)  # Expected: [[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]]
print(normalized)    # Expected: [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]]
```