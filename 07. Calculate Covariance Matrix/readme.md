# Calculate Covariance Matrix

## 1. Problem Overview

### What is a Covariance Matrix?

A covariance matrix is a key concept in statistics and machine learning that measures how much two features vary together. It is widely used in data analysis, Principal Component Analysis (PCA), and multivariate modeling.

For a set of feature vectors, the covariance matrix shows the covariance between every pair of features in a symmetric matrix.

### The Problem

Given a list of feature vectors (each inner list contains observations for one feature), write a Python function to calculate the covariance matrix. The function should return the matrix as a list of lists.

If the input has `n` features, the output will be an `n x n` matrix where element `[i][j]` represents the covariance between feature `i` and feature `j`.

---

## 2. Code Explanation With Comments

```python
import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Number of features (rows)
    n_features = len(vectors)
    # Number of observations per feature (columns)
    n_observations = len(vectors[0])

    # Initialize an empty covariance matrix with zeros
    covariance_matrix = [[0 for _ in range(n_features)] for _ in range(n_features)]

    # Calculate mean of each feature
    means = [sum(feature) / n_observations for feature in vectors]

    # Compute covariance for each pair of features
    for i in range(n_features):
        for j in range(i, n_features):
            covariance = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                             for k in range(n_observations)) / (n_observations - 1)
            # Covariance matrix is symmetric, so set both [i][j] and [j][i]
            covariance_matrix[i][j] = covariance_matrix[j][i] = covariance

    return covariance_matrix
```

### Key Points to Remember

* Covariance measures how two features vary together.
* Covariance matrix is always symmetric.
* The formula divides by `(n_observations - 1)` to account for sample covariance.
* `covariance_matrix[i][j]` is equal to `covariance_matrix[j][i]`.

---

## 3. Solution Approach and Logic

1. **Determine the number of features and observations**

   * Each inner list represents a feature; all features should have the same number of observations.

2. **Compute feature means**

   * The mean of each feature is required to calculate deviations.

3. **Compute pairwise covariances**

   * For every pair of features `(i, j)`, compute `sum((x_i - mean_i)*(x_j - mean_j)) / (n-1)`
   * Store the result in both `[i][j]` and `[j][i]` because covariance is symmetric.

4. **Return the final covariance matrix**

---

## 4. Example Calculation

### Input

```python
[[1, 2, 3], [4, 5, 6]]
```

### Step-by-Step

* Feature 1 mean: (1+2+3)/3 = 2.0
* Feature 2 mean: (4+5+6)/3 = 5.0
* Covariance (feature 1 & feature 1): ((1-2)^2 + (2-2)^2 + (3-2)^2)/2 = 1.0
* Covariance (feature 1 & feature 2): ((1-2)*(4-5) + (2-2)*(5-5) + (3-2)*(6-5))/2 = 1.0
* Covariance (feature 2 & feature 2): ((4-5)^2 + (5-5)^2 + (6-5)^2)/2 = 1.0

### Output

```python
[[1.0, 1.0], [1.0, 1.0]]
```

---

## 5. Test Cases

1. Small 2-feature dataset
2. 3-feature dataset with 4 observations
3. 3-feature dataset with larger numbers

These test cases verify that the function works for different numbers of features and observations.

```python
def test_calculate_covariance_matrix():
    # Test case 1
    vectors = [[1, 2, 3], [4, 5, 6]]
    expected = [[1.0, 1.0], [1.0, 1.0]]
    assert calculate_covariance_matrix(vectors) == expected
    
    # Test case 2
    vectors = [[1, 2, 3, 4], [2, 3, 4, 5], [5, 6, 7, 8]]
    expected = [[1.6666666666666667, 1.6666666666666667, 1.666666666666667],
                [1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0]]
    assert calculate_covariance_matrix(vectors) == expected
    
    # Test case 3
    vectors = [[10, 20, 30], [20, 30, 40], [30, 40, 50]]
    expected = [[100.0, 100.0, 100.0],
                [100.0, 100.0, 100.0],
                [100.0, 100.0, 100.0]]
    assert calculate_covariance_matrix(vectors) == expected
```
