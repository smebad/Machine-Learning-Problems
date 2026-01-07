# Linear Regression Using Normal Equation

## 1. Problem Overview

### What is Linear Regression Using the Normal Equation?

Linear regression is a fundamental machine learning technique used to model the relationship between a set of features (independent variables) and a target variable (dependent variable). The **normal equation** provides a closed-form solution to compute the coefficients (weights) that minimize the mean squared error without iterative optimization.

Given a feature matrix `X` and a target vector `y`, the coefficients `theta` are computed as:

```
theta = (X^T X)^(-1) X^T y
```

This formula calculates the exact best-fit line (or hyperplane in multiple dimensions) directly.

### The Problem

Write a Python function that:

* Takes `X` (matrix of features) and `y` (target vector)
* Computes the regression coefficients using the normal equation
* Returns the coefficients rounded to four decimal places

---

## 2. Code Explanation (With Comments)

```python
import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Convert X and y to NumPy arrays for matrix operations
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)  # Ensure y is a column vector

    # Compute the transpose of X
    X_transpose = X.T

    # Compute theta using the normal equation formula
    theta = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)

    # Round the coefficients to 4 decimal places and convert to a flat list
    theta = np.round(theta, 4).flatten().tolist()

    return theta
```

### Key Points to Remember

* `X^T` is the transpose of X
* `np.linalg.inv()` computes the matrix inverse
* Dot products are used to compute `X^T X` and `X^T y`
* Reshaping `y` ensures proper matrix multiplication
* Rounding handles numerical precision and small floating-point errors

---

## 3. Solution Approach and Logic

1. **Prepare the Data**

   * Ensure `X` is a matrix and `y` is a column vector for correct operations

2. **Compute the Normal Equation**

   * Multiply the transpose of X by X: `X^T X`
   * Invert the resulting matrix: `(X^T X)^(-1)`
   * Multiply the inverse with the transpose of X and then with `y` to get coefficients

3. **Return Rounded Coefficients**

   * Flatten the result to a 1D list and round each coefficient to four decimal places

---

## 4. Example Calculation

### Input

```python
X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
```

### Step-by-Step

* Compute X^T X:

```
[[3, 6],
 [6, 14]]
```

* Compute X^T y:

```
[[6],
 [14]]
```

* Invert X^T X and multiply with X^T y:

```
theta = [[0.0], [1.0]]
```

* Flatten and round: `[0.0, 1.0]`

### Output

```python
[0.0, 1.0]
```

---

## 5. Test Cases

* Test Case 1: Perfect linear relation with feature 1 and target
* Test Case 2: Different feature offsets still yielding a perfect slope
* Test Case 3: Larger values and different feature combinations with exact fit

```python
if __name__ == "__main__":
    
      # Test Case 1
  X = [[1, 1], [1, 2], [1, 3]]
  y = [1, 2, 3]
  coefficients = linear_regression_normal_equation(X, y)
  print(coefficients)  # Output: [-0.0, 1.0]

  # Test Case 2
  X = [[1, 0], [1, 1], [1, 2]]
  y = [1, 2, 3]
  coefficients = linear_regression_normal_equation(X, y)
  print(coefficients)  # Output: [1.0, 1.0]

  # Test Case 3
  X = [[1, 2], [1, 3], [1, 4]]
  y = [2, 3, 4]
  coefficients = linear_regression_normal_equation(X, y)
  print(coefficients)  # Output: [-0.0, 1.0]
```
 
